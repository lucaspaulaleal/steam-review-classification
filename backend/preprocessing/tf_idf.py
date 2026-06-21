# backend/preprocessing/tf_idf.py

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from math import log
from utils import binary_search_tuples, sorted_insert_tuple


def _unique_tokens(tokens):
    """Retorna lista de tokens únicos sem usar set/dict."""
    seen = []
    for token in tokens:
        left, right, found = 0, len(seen) - 1, False
        while left <= right:
            mid = (left + right) // 2
            if seen[mid] == token:
                found = True
                break
            elif seen[mid] < token:
                left = mid + 1
            else:
                right = mid - 1
        if not found:
            seen.insert(left, token)
    return seen


def _count_token(tokens, target):
    count = 0
    for token in tokens:
        if token == target:
            count += 1
    return count


def _build_df_table(documents):
    """
    Percorre todos os documentos UMA única vez e constrói uma tabela de
    Document Frequency ordenada alfabeticamente por token.

    Retorna:
        df_table: lista de tuplas [(token, df_count), ...] ordenada por token.

    Complexidade: O(D * T * log T) onde D = docs, T = tokens únicos por doc.
    Lookup posterior: O(log V) via binary_search_tuples.
    """
    df_table = []

    for _, tokens in documents:
        unique = _unique_tokens(tokens)
        for token in unique:
            pos = binary_search_tuples(df_table, token)
            if pos == -1:
                # Token novo: insere ordenado
                sorted_insert_tuple(df_table, (token, 1))
            else:
                # Token existente: incrementa
                df_table[pos] = (token, df_table[pos][1] + 1)

    return df_table


def calculate_tf_idf(documents):
    """
    Calcula TF-IDF manualmente usando listas.

    O Document Frequency é pré-computado em _build_df_table (uma única passagem),
    depois consultado via busca binária — eliminando o loop O(N²) original.

    Entrada:
        [
            ("R1", ["fps", "lag", "fps"]),
            ("R2", ["textura", "resolucao"]),
        ]

    Saída:
        [
            ("R1", [("fps", 0.5406), ("lag", 0.2703)]),
            ("R2", [("textura", 0.3466), ("resolucao", 0.3466)]),
        ]
    """
    total_documents = len(documents)
    result = []

    # Passo 1: construir tabela de DF em uma única passagem — O(D * T * log V)
    df_table = _build_df_table(documents)

    # Passo 2: calcular TF-IDF por documento usando busca binária no df_table
    for doc_idx in range(total_documents):
        review_label, tokens = documents[doc_idx]
        unique_tokens = _unique_tokens(tokens)
        weighted_terms = []

        if len(tokens) == 0:
            result.append((review_label, weighted_terms))
            continue

        for token in unique_tokens:
            # TF: importância local da palavra na review.
            term_frequency = _count_token(tokens, token) / len(tokens)

            # DF: busca binária O(log V) em vez de varredura O(D).
            pos = binary_search_tuples(df_table, token)
            document_frequency = df_table[pos][1] if pos != -1 else 0

            # IDF suavizado evita divisão por zero e reduz palavras comuns.
            inverse_document_frequency = (
                log((1 + total_documents) / (1 + document_frequency)) + 1
            )
            weighted_terms.append((token, term_frequency * inverse_document_frequency))

        result.append((review_label, weighted_terms))

    return result