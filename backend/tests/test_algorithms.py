from backend.graph.builder import build_tripartite_graph, mock_documents, mock_seed_groups
from backend.graph.pmi import calculate_pmi
from backend.preprocessing.tf_idf import calculate_tf_idf
from backend.propagation.label_propagation import classify_reviews, label_propagation


def _find_tuple_by_first(items, target):
    for item in items:
        if item[0] == target:
            return item
    return None


def _find_pair(items, word_a, word_b):
    for item in items:
        if item[0] == word_a and item[1] == word_b:
            return item
        if item[0] == word_b and item[1] == word_a:
            return item
    return None


def _find_classification(items, review_label):
    for item in items:
        if item[0] == review_label:
            return item
    return None


def test_tf_idf_returns_weighted_terms_by_review():
    documents = [
        ("R1", ["fps", "fps", "lag"]),
        ("R2", ["historia", "enredo"]),
    ]

    result = calculate_tf_idf(documents)
    r1 = _find_tuple_by_first(result, "R1")

    assert r1 is not None
    assert len(r1[1]) == 2
    assert _find_tuple_by_first(r1[1], "fps")[1] > _find_tuple_by_first(r1[1], "lag")[1]


def test_pmi_returns_positive_word_cooccurrence_edges():
    documents = [
        ("R1", ["fps", "lag"]),
        ("R2", ["fps", "crash"]),
        ("R3", ["historia", "enredo"]),
    ]

    result = calculate_pmi(documents)

    assert _find_pair(result, "fps", "lag") is not None
    assert _find_pair(result, "historia", "enredo") is not None


def test_tripartite_graph_contains_expected_layers_and_edges():
    graph = build_tripartite_graph(mock_documents(), mock_seed_groups())

    assert graph.get_node_type("R1") == "review"
    assert graph.get_node_type("word:fps") == "word"
    assert graph.get_node_type("Performance") == "category"
    assert len(graph.get_neighbors("R1")) > 0
    assert ("Performance", 1.0) in graph.get_neighbors("word:fps")


def test_label_propagation_classifies_mock_reviews():
    graph = build_tripartite_graph(mock_documents(), mock_seed_groups())
    scores = label_propagation(graph, iterations=30, threshold=0.0001)
    classifications = classify_reviews(graph, scores)

    r1 = _find_classification(classifications, "R1")
    r2 = _find_classification(classifications, "R2")
    r3 = _find_classification(classifications, "R3")
    r4 = _find_classification(classifications, "R4")

    assert r1[1] == "Performance"
    assert r2[1] == "Graficos"
    assert r3[1] == "Gameplay"
    assert r4[1] == "Narrativa"
