import pytest
from backend.graph.graph import Graph


def test_graph_add_node():
    g = Graph()
    idx1 = g.add_node("Review1")
    idx2 = g.add_node("fps")
    
    assert idx1 == 0
    assert idx2 == 1
    assert g.labels == ["Review1", "fps"]
    assert len(g.adj) == 2


def test_graph_add_edge():
    g = Graph()
    g.add_edge("Review1", "fps", 0.82)
    
    # "Review1" receives index 0, "fps" receives index 1
    neighbors = g.get_neighbors("Review1")
    assert len(neighbors) == 1
    assert neighbors[0] == ("fps", 0.82)


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
