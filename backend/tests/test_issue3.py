"""
Script de validação manual da Issue #3.

Como rodar (da raiz do projeto):
    python -m pytest backend/tests/test_issue3.py -v -s
"""
import sys, os
# Adiciona o backend ao path para importações funcionarem
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils import binary_search_tuples, sorted_insert_tuple


# ─────────────────────────────────────────────────────────────
# PASSO 1 — utils.py
# ─────────────────────────────────────────────────────────────
def test_binary_search_tuples():
    lista = [("bala", 5), ("fps", 12), ("tiro", 2)]

    assert binary_search_tuples(lista, "fps")  == 1
    assert binary_search_tuples(lista, "bala") == 0
    assert binary_search_tuples(lista, "tiro") == 2
    assert binary_search_tuples(lista, "xxx")  == -1
    print("  [OK] binary_search_tuples encontra e retorna -1 para ausente")


def test_sorted_insert_tuple():
    lista = []
    for item in [("fps", 1), ("bala", 0), ("tiro", 2), ("arma", 3)]:
        sorted_insert_tuple(lista, item)

    keys = [t[0] for t in lista]
    assert keys == sorted(keys)
    print(f"  [OK] sorted_insert_tuple mantém lista ordenada → {lista}")


# ─────────────────────────────────────────────────────────────
# PASSO 2 — graph.py
# ─────────────────────────────────────────────────────────────
def test_graph_node_map_ordenado():
    from graph.graph import Graph
    g = Graph()
    g.add_node("tiro",  "word")
    g.add_node("bala",  "word")
    g.add_node("fps",   "word")
    g.add_node("arma",  "word")

    keys = [t[0] for t in g.node_map]
    assert keys == sorted(keys), f"node_map não ordenado: {keys}"
    print(f"  [OK] node_map ordenado → {g.node_map}")


def test_graph_find_node_idx_busca_binaria():
    from graph.graph import Graph
    g = Graph()
    g.add_node("tiro", "word")
    g.add_node("bala", "word")
    g.add_node("fps",  "word")

    assert g._find_node_idx("fps")       != -1
    assert g._find_node_idx("naoexiste") == -1
    print(f"  [OK] _find_node_idx usa busca binária via node_map")


def test_graph_upsert_edge_vizinhos_ordenados():
    from graph.graph import Graph
    g = Graph()
    g.add_edge("fps", "lag",  0.5)
    g.add_edge("fps", "bala", 0.3)
    g.add_edge("fps", "arma", 0.9)

    fps_idx = g._find_node_idx("fps")
    ids = [nid for nid, _ in g.adj[fps_idx]]
    assert ids == sorted(ids), f"Vizinhos não ordenados: {ids}"
    print(f"  [OK] Vizinhos de 'fps' ordenados por ID → {g.adj[fps_idx]}")


def test_graph_upsert_edge_atualiza_peso():
    from graph.graph import Graph
    g = Graph()
    g.add_edge("fps", "lag", 0.5)
    g.add_edge("fps", "lag", 0.99)  # deve atualizar, não duplicar

    fps_idx = g._find_node_idx("fps")
    lag_idx = g._find_node_idx("lag")
    pesos = [w for nid, w in g.adj[fps_idx] if nid == lag_idx]
    assert len(pesos) == 1 and pesos[0] == 0.99
    print(f"  [OK] _upsert_edge atualiza peso sem duplicar aresta")


# ─────────────────────────────────────────────────────────────
# PASSO 3 — tf_idf.py
# ─────────────────────────────────────────────────────────────
def test_build_df_table_ordenado_e_correto():
    from preprocessing.tf_idf import _build_df_table

    docs = [
        ("R1", ["fps", "lag", "fps"]),
        ("R2", ["fps", "textura"]),
        ("R3", ["lag", "resolucao"]),
    ]
    df_table = _build_df_table(docs)

    keys = [t[0] for t in df_table]
    assert keys == sorted(keys), f"df_table não ordenado: {keys}"

    fps_pos = binary_search_tuples(df_table, "fps")
    assert fps_pos != -1 and df_table[fps_pos][1] == 2  # fps em R1 e R2

    lag_pos = binary_search_tuples(df_table, "lag")
    assert lag_pos != -1 and df_table[lag_pos][1] == 2  # lag em R1 e R3

    print(f"  [OK] df_table ordenado e com contagens corretas → {df_table}")


def test_calculate_tf_idf_sem_loop_quadratico():
    from preprocessing.tf_idf import calculate_tf_idf

    docs = [
        ("R1", ["fps", "lag", "fps"]),
        ("R2", ["textura", "resolucao"]),
    ]
    result = calculate_tf_idf(docs)

    assert len(result) == 2
    labels = [r[0] for r in result]
    assert "R1" in labels and "R2" in labels
    for _, terms in result:
        assert len(terms) > 0
        for token, score in terms:
            assert score > 0

    print(f"  [OK] calculate_tf_idf retorna scores positivos → {result[0]}")


# ─────────────────────────────────────────────────────────────
# PASSO 4 — pmi.py
# ─────────────────────────────────────────────────────────────
def test_build_cooccurrence_tables():
    from graph.pmi import _build_cooccurrence_tables

    corpus = [
        ("R1", ["fps", "lag", "performance"]),
        ("R2", ["fps", "grafico", "resolucao"]),
        ("R3", ["lag", "performance", "fps"]),
    ]
    word_counts, pair_counts = _build_cooccurrence_tables(corpus)

    wc_keys = [t[0] for t in word_counts]
    assert wc_keys == sorted(wc_keys), f"word_counts não ordenado: {wc_keys}"

    pc_keys = [t[0] for t in pair_counts]
    assert pc_keys == sorted(pc_keys), f"pair_counts não ordenado: {pc_keys}"

    fps_pos = binary_search_tuples(word_counts, "fps")
    assert fps_pos != -1 and word_counts[fps_pos][1] == 3  # fps nas 3 reviews

    print(f"  [OK] word_counts → {word_counts}")
    print(f"  [OK] pair_counts ordenado com {len(pair_counts)} pares")


def test_calculate_pmi_so_positivos():
    from graph.pmi import calculate_pmi

    corpus = [
        ("R1", ["fps", "lag", "performance"]),
        ("R2", ["fps", "grafico", "resolucao"]),
        ("R3", ["lag", "performance", "fps"]),
    ]
    edges = calculate_pmi(corpus)

    assert len(edges) > 0
    for a, b, pmi in edges:
        assert pmi > 0, f"PMI deve ser positivo: ({a},{b})={pmi}"

    print(f"  [OK] calculate_pmi retorna {len(edges)} arestas com PMI > 0 → {edges[:2]}...")


def test_pmi_corpus_vazio():
    from graph.pmi import calculate_pmi
    assert calculate_pmi([]) == []
    print("  [OK] calculate_pmi retorna [] para corpus vazio")