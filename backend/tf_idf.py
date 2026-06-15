#backend/tf_idf.py

from math import log


def _find_index(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


def _unique_tokens(tokens):
    unique = []
    for token in tokens:
        #Mantem uma palavra uma unica vez, sem usar set.
        if _find_index(unique, token) == -1:
            unique.append(token)
    return unique


def _count_token(tokens, target):
    count = 0
    for token in tokens:
        if token == target:
            count += 1
    return count


def calculate_tf_idf(documents):
    """
    Calcula TF-IDF manualmente usando listas.

    Entrada:
        [
            ("R1", ["fps", "lag", "fps"]),
            ("R2", ["textura", "resolucao"]),
        ]

    Saida:
        [
            ("R1", [("fps", 0.5406), ("lag", 0.2703)]),
            ("R2", [("textura", 0.3466), ("resolucao", 0.3466)]),
        ]
    """
    total_documents = len(documents)
    result = []

    for doc_idx in range(total_documents):
        review_label, tokens = documents[doc_idx]
        #TF-IDF precisa calcular cada palavra distinta da review.
        unique_tokens = _unique_tokens(tokens)
        weighted_terms = []

        if len(tokens) == 0:
            result.append((review_label, weighted_terms))
            continue

        for token in unique_tokens:
            #TF mede a importancia local da palavra na review.
            term_frequency = _count_token(tokens, token) / len(tokens)

            #DF conta em quantas reviews a palavra aparece.
            document_frequency = 0
            for other_idx in range(total_documents):
                _, other_tokens = documents[other_idx]
                if _find_index(_unique_tokens(other_tokens), token) != -1:
                    document_frequency += 1

            #IDF suavizado evita divisao por zero e reduz palavras comuns.
            inverse_document_frequency = log((1 + total_documents) / (1 + document_frequency)) + 1
            weighted_terms.append((token, term_frequency * inverse_document_frequency))

        result.append((review_label, weighted_terms))

    return result
