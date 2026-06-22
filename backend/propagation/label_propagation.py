#backend/propagation/label_propagation.py


def _binary_search(items, target):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def _find_insert_position(items, target):
    left = 0
    right = len(items)

    while left < right:
        mid = (left + right) // 2
        if items[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def _category_labels(graph):
    categories = []
    for i in range(graph.size()):
        #Somente nos de categoria viram dimensoes do vetor de scores.
        if graph.node_types[i] == "category":
            insert_pos = _find_insert_position(categories, graph.labels[i])
            categories.insert(insert_pos, graph.labels[i])
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


def _initial_scores(graph, categories):
    scores = []

    for node_idx in range(graph.size()):
        node_scores = _empty_score_vector(categories)

        if graph.node_types[node_idx] == "category":
            #Categoria comeca fixa nela mesma, como rotulo conhecido.
            category_idx = _binary_search(categories, graph.labels[node_idx])
            if category_idx != -1:
                label, _ = node_scores[category_idx]
                node_scores[category_idx] = (label, 1.0)

        scores.append(node_scores)

    return scores


def _propagate_once(graph, scores, categories, initial_scores, damping_factor):
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
            
        # Mistura com o score inicial usando o damping_factor
        blended = []
        for category in categories:
            prop_val = _get_score(propagated, category)
            init_val = _get_score(initial_scores[node_idx], category)
            final_val = (damping_factor * prop_val) + ((1.0 - damping_factor) * init_val)
            blended.append((category, final_val))

        new_scores.append(blended)

    return new_scores


def _scores_result(graph, scores):
    result = []
    for node_idx in range(graph.size()):
        result.append((graph.labels[node_idx], scores[node_idx]))
    return result


def label_propagation(graph, iterations=20, threshold=0.001, damping_factor=0.85):
    """
    Propaga os rotulos das categorias pelo grafo.

    O grafo deve ter arestas bidirecionais nos caminhos em que a informacao
    precisa circular. Nos de categoria ficam fixos com score 1.0 neles mesmos.
    """
    categories = _category_labels(graph)
    initial = _initial_scores(graph, categories)
    scores = initial

    for _ in range(iterations):
        new_scores = _propagate_once(graph, scores, categories, initial, damping_factor)

        if _max_delta(scores, new_scores, categories) < threshold:
            #Para quando as mudancas ficam pequenas o suficiente.
            scores = new_scores
            break

        scores = new_scores

    return _scores_result(graph, scores)


def label_propagation_with_history(graph, iterations=20, threshold=0.001, damping_factor=0.85):
    """
    Executa a propagacao e tambem registra o max_delta por iteracao.
    Esse historico serve como evidencia matematica de convergencia.
    """
    categories = _category_labels(graph)
    initial = _initial_scores(graph, categories)
    scores = initial
    history = []

    for iteration in range(1, iterations + 1):
        new_scores = _propagate_once(graph, scores, categories, initial, damping_factor)
        max_delta = _max_delta(scores, new_scores, categories)
        history.append((iteration, max_delta))

        scores = new_scores
        if max_delta < threshold:
            break

    return _scores_result(graph, scores), history


def classify_reviews(graph, scores):
    """
    Retorna a melhor categoria para cada no de review aplicando Class Mass Normalization (CMN).
    Aplica a normalizacao pelas massas totais acumuladas nas reviews para evitar que 
    categorias superconectadas (hubs) dominem a classificacao.
    """
    classifications = []
    
    # 1. Calcular a massa total (soma de scores) de cada categoria em todos os nos de review
    class_mass = {}
    for node_idx in range(graph.size()):
        if graph.node_types[node_idx] != "review":
            continue
            
        label = graph.labels[node_idx]
        node_scores = []
        for score_label, score_values in scores:
            if score_label == label:
                node_scores = score_values
                break
                
        for category, value in node_scores:
            class_mass[category] = class_mass.get(category, 0.0) + value

    # Evitar divisao por zero caso uma categoria tenha massa 0
    for cat in class_mass:
        if class_mass[cat] == 0.0:
            class_mass[cat] = 1.0

    # 2. Classificar cada review ajustando o score pela massa da classe
    for node_idx in range(graph.size()):
        if graph.node_types[node_idx] != "review":
            continue

        label = graph.labels[node_idx]
        node_scores = []
        for score_label, score_values in scores:
            if score_label == label:
                node_scores = score_values
                break

        best_category = "Outros"
        best_score = 0.0
        for category, value in node_scores:
            # A categoria final e a de maior score normalizado (adjusted_score)
            adjusted_score = value / class_mass.get(category, 1.0)
            if adjusted_score > best_score:
                best_category = category
                best_score = adjusted_score

        classifications.append((label, best_category, best_score, node_scores))

    return classifications
