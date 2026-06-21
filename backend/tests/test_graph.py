from backend.graph.graph import Graph


def test_graph_add_node():
    g = Graph()
    idx1 = g.add_node("Review1")
    idx2 = g.add_node("fps")
    
    assert idx1 == 0
    assert idx2 == 1
    assert g.labels == ["Review1", "fps"]
    assert len(g.adj) == 2
    assert g.node_map == [("Review1", 0), ("fps", 1)]


def test_graph_add_node_keeps_binary_search_index_sorted():
    g = Graph()
    idx_z = g.add_node("word:zeta")
    idx_a = g.add_node("word:alpha")
    idx_m = g.add_node("word:middle")

    assert g.node_map == [
        ("word:alpha", idx_a),
        ("word:middle", idx_m),
        ("word:zeta", idx_z),
    ]
    assert g._find_node_idx("word:zeta") == idx_z
    assert g._find_node_idx("word:alpha") == idx_a
    assert g._find_node_idx("word:middle") == idx_m


def test_graph_reuses_existing_node_and_updates_unknown_type():
    g = Graph()
    first_idx = g.add_node("word:fps")
    second_idx = g.add_node("word:fps", "word")

    assert first_idx == second_idx
    assert g.size() == 1
    assert g.get_node_type("word:fps") == "word"


def test_graph_add_edge():
    g = Graph()
    g.add_edge("Review1", "fps", 0.82)
    
    # "Review1" receives index 0, "fps" receives index 1
    neighbors = g.get_neighbors("Review1")
    assert len(neighbors) == 1
    assert neighbors[0] == ("fps", 0.82)


def test_graph_updates_existing_edge_weight_without_duplicate():
    g = Graph()
    g.add_edge("Review1", "fps", 0.82)
    g.add_edge("Review1", "fps", 0.91)

    assert g.get_neighbors("Review1") == [("fps", 0.91)]


def test_graph_add_bidirectional_edge():
    g = Graph()
    g.add_edge("fps", "lag", 0.74, bidirectional=True)

    assert g.get_neighbors("fps") == [("lag", 0.74)]
    assert g.get_neighbors("lag") == [("fps", 0.74)]


def test_graph_tracks_node_type():
    g = Graph()
    g.add_node("R1", "review")
    g.add_node("word:fps", "word")
    g.add_node("Performance", "category")

    assert g.get_node_type("R1") == "review"
    assert g.get_node_type("word:fps") == "word"
    assert g.get_node_type("Performance") == "category"


def test_graph_returns_empty_values_for_missing_nodes_and_invalid_indices():
    g = Graph()
    g.add_node("R1", "review")

    assert g.get_neighbors("missing") == []
    assert g.get_neighbors_by_idx(-1) == []
    assert g.get_neighbors_by_idx(99) == []
    assert g.get_node_type("missing") == ""
    assert g._find_node_idx("missing") == -1
