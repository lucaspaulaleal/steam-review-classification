#backend/label_propagation.py


def _find_index(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


def _category_labels(graph):
    categories = []
    for i in range(graph.size()):
        #Somente nos de categoria viram dimensoes do vetor de scores.
        if graph.node_types[i] == "category":
            categories.append(graph.labels[i])
    return categories


def _empty_score_vector(categories):
    scores = []
    for category in categories:
        scores.append((category, 0.0))
    return scores


def _get_score(scores, category):
    for label, value in scores:
        if label == category:
            return value
    return 0.0


def _add_score(scores, category, value):
    for i in range(len(scores)):
        label, current = scores[i]
        if label == category:
            scores[i] = (label, current + value)
            return


def _normalize(scores):
    total = 0.0
    for _, value in scores:
        total += value

    if total == 0.0:
        return scores

    #Depois de somar influencias, deixamos os scores em escala comparavel.
    normalized = []
    for label, value in scores:
        normalized.append((label, value / total))
    return normalized


def _max_delta(old_scores, new_scores, categories):
    max_delta = 0.0
    for node_idx in range(len(old_scores)):
        for category in categories:
            delta = abs(
                _get_score(old_scores[node_idx], category)
                - _get_score(new_scores[node_idx], category)
            )
            if delta > max_delta:
                max_delta = delta
    return max_delta


def label_propagation(graph, iterations=20, threshold=0.001):
    """
    Propaga os rotulos das categorias pelo grafo.

    O grafo deve ter arestas bidirecionais nos caminhos em que a informacao
    precisa circular. Nos de categoria ficam fixos com score 1.0 neles mesmos.
    """
    categories = _category_labels(graph)
    scores = []

    for node_idx in range(graph.size()):
        node_scores = _empty_score_vector(categories)

        if graph.node_types[node_idx] == "category":
            #Categoria comeca fixa nela mesma, como rotulo conhecido.
            category_idx = _find_index(categories, graph.labels[node_idx])
            if category_idx != -1:
                label, _ = node_scores[category_idx]
                node_scores[category_idx] = (label, 1.0)

        scores.append(node_scores)

    for _ in range(iterations):
        new_scores = []

        for node_idx in range(graph.size()):
            if graph.node_types[node_idx] == "category":
                #Seeds finais nao mudam durante a propagacao.
                new_scores.append(scores[node_idx])
                continue

            propagated = _empty_score_vector(categories)
            total_weight = 0.0

            for neighbor_idx, weight in graph.get_neighbors_by_idx(node_idx):
                #Cada vizinho contribui proporcionalmente ao peso da aresta.
                total_weight += weight
                for category in categories:
                    _add_score(
                        propagated,
                        category,
                        _get_score(scores[neighbor_idx], category) * weight,
                    )

            if total_weight > 0.0:
                #Divide pela soma dos pesos para evitar favorecer nos muito conectados.
                scaled = []
                for category, value in propagated:
                    scaled.append((category, value / total_weight))
                propagated = _normalize(scaled)

            new_scores.append(propagated)

        if _max_delta(scores, new_scores, categories) < threshold:
            #Para quando as mudancas ficam pequenas o suficiente.
            scores = new_scores
            break

        scores = new_scores

    result = []
    for node_idx in range(graph.size()):
        result.append((graph.labels[node_idx], scores[node_idx]))
    return result


def classify_reviews(graph, scores):
    """Retorna a melhor categoria para cada no de review."""
    classifications = []

    for node_idx in range(graph.size()):
        if graph.node_types[node_idx] != "review":
            continue

        label = graph.labels[node_idx]
        node_scores = []
        for score_label, score_values in scores:
            if score_label == label:
                node_scores = score_values
                break

        best_category = ""
        best_score = -1.0
        for category, value in node_scores:
            #A categoria final e a de maior score.
            if value > best_score:
                best_category = category
                best_score = value

        classifications.append((label, best_category, best_score, node_scores))

    return classifications
