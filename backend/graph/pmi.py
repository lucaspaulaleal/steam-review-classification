# backend/graph/pmi.py

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from math import log
from utils import binary_search_tuples, sorted_insert_tuple


def _unique_tokens(tokens):
    """Retorna tokens únicos de uma review, ordenados — sem usar set/dict."""
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


def _ordered_pair(a, b):
    """Garante que ("fps", "lag") e ("lag", "fps") sejam o mesmo par."""
    if a <= b:
        return (a, b)
    return (b, a)


def _increment_in_table(table, key):
    """
    Incrementa contador de key na tabela ordenada.
    Se não existir, insere com count=1 mantendo a ordem.
    Busca: O(log N). Inserção: O(N).
    """
    pos = binary_search_tuples(table, key)
    if pos == -1:
        sorted_insert_tuple(table, (key, 1))
    else:
        table[pos] = (key, table[pos][1] + 1)


def _build_cooccurrence_tables(corpus):
    """
    Percorre o corpus uma única vez e constrói:
      - word_counts: [(token, contagem_de_docs), ...] ordenado por token
      - pair_counts: [((tokenA, tokenB), contagem_de_docs), ...] ordenado por par

    Retorna:
        (word_counts, pair_counts)
    """
    word_counts = []
    pair_counts = []

    for _, tokens in corpus:
        unique = _unique_tokens(tokens)

        # Contagem de documentos por palavra
        for token in unique:
            _increment_in_table(word_counts, token)

        # Contagem de documentos por par de palavras
        for i in range(len(unique)):
            for j in range(i + 1, len(unique)):
                pair = _ordered_pair(unique[i], unique[j])
                _increment_in_table(pair_counts, pair)

    return word_counts, pair_counts


def calculate_pmi(corpus, threshold=0.0):
    """
    Mede coocorrência estatística entre palavras usando PMI.

    A unidade de coocorrência é o documento/review: duas palavras coocorrem
    quando aparecem na mesma review.

    As tabelas de contagem são construídas em uma única passagem pelo corpus
    e consultadas via busca binária — eliminando o _get_count O(N) do loop original.

    Retorna apenas pares com PMI positivo.
    """
    total_documents = len(corpus)
    if total_documents == 0:
        return []

    # Passo 1: construir tabelas ordenadas em uma única passagem
    word_counts, pair_counts = _build_cooccurrence_tables(corpus)

    # Passo 2: calcular PMI para cada par usando busca binária
    pmi_edges = []
    for pair, pair_count in pair_counts:
        word_a, word_b = pair

        pos_a = binary_search_tuples(word_counts, word_a)
        pos_b = binary_search_tuples(word_counts, word_b)

        if pos_a == -1 or pos_b == -1:
            continue

        count_a = word_counts[pos_a][1]
        count_b = word_counts[pos_b][1]

        if count_a == 0 or count_b == 0:
            continue

        probability_pair = pair_count / total_documents
        probability_a = count_a / total_documents
        probability_b = count_b / total_documents

        # PMI clássico
        pmi = log(probability_pair / (probability_a * probability_b))
        
        # NPMI (Normalized PMI): normaliza o score entre [-1, 1]
        npmi = pmi / -log(probability_pair)

        if npmi > threshold:
            # NPMI negativo não ajuda como ligação semântica neste grafo.
            pmi_edges.append((word_a, word_b, npmi))

    return pmi_edges    