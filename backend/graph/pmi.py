#backend/graph/pmi.py

from math import log


def _find_index(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


def _unique_tokens(tokens):
    unique = []
    for token in tokens:
        #PMI considera presenca na review, nao repeticao bruta.
        if _find_index(unique, token) == -1:
            unique.append(token)
    return unique


def _add_or_increment(counter, item):
    #Counter manual em lista para evitar dict.
    for i in range(len(counter)):
        value, count = counter[i]
        if value == item:
            counter[i] = (value, count + 1)
            return
    counter.append((item, 1))


def _get_count(counter, item):
    for value, count in counter:
        if value == item:
            return count
    return 0


def _ordered_pair(a, b):
    #Garante que (fps, lag) e (lag, fps) sejam o mesmo par.
    if a <= b:
        return (a, b)
    return (b, a)


def calculate_pmi(corpus):
    """
    Mede coocorrencia estatistica entre palavras usando PMI.

    A unidade de coocorrencia aqui e o documento/review: duas palavras coocorrem
    quando aparecem na mesma review. O retorno contem apenas pares positivos.
    """
    total_documents = len(corpus)
    word_document_counts = []
    pair_document_counts = []

    if total_documents == 0:
        return []

    for _, tokens in corpus:
        #Cada review vira uma janela de coocorrencia.
        unique = _unique_tokens(tokens)

        for token in unique:
            _add_or_increment(word_document_counts, token)

        for i in range(len(unique)):
            for j in range(i + 1, len(unique)):
                #Conta cada par de palavras que apareceu junto na review.
                pair = _ordered_pair(unique[i], unique[j])
                _add_or_increment(pair_document_counts, pair)

    pmi_edges = []
    for pair, pair_count in pair_document_counts:
        word_a, word_b = pair
        count_a = _get_count(word_document_counts, word_a)
        count_b = _get_count(word_document_counts, word_b)

        if count_a == 0 or count_b == 0:
            continue

        probability_pair = pair_count / total_documents
        probability_a = count_a / total_documents
        probability_b = count_b / total_documents
        #PMI alto indica associacao acima do acaso.
        pmi = log(probability_pair / (probability_a * probability_b))

        if pmi > 0:
            #PMI negativo nao ajuda como ligacao semantica neste grafo.
            pmi_edges.append((word_a, word_b, pmi))

    return pmi_edges
