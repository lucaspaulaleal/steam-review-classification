#backend/graph/builder.py

from backend.graph.graph import Graph
from backend.graph.pmi import calculate_pmi
from backend.preprocessing.tf_idf import calculate_tf_idf


def _find_index(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


def _category_seed_pairs(seed_groups):
    pairs = []
    for category, seeds in seed_groups:
        for seed in seeds:
            #Transforma grupos em pares simples: palavra -> categoria.
            pairs.append((seed, category))
    return pairs


def build_tripartite_graph(documents, seed_groups):
    """
    Constroi o grafo tripartido:
    - review -> palavra com peso TF-IDF
    - palavra <-> palavra com peso PMI
    - palavra -> categoria com peso fixo de seed

    Tudo e representado em listas, sem bibliotecas prontas de grafo.
    """
    graph = Graph()
    #Pesos das tres familias de arestas do grafo.
    tf_idf_weights = calculate_tf_idf(documents)
    pmi_edges = calculate_pmi(documents)
    seed_pairs = _category_seed_pairs(seed_groups)

    for category, _ in seed_groups:
        #Categorias entram primeiro porque sao os rotulos fixos.
        graph.add_node(category, "category")

    for review_label, weighted_terms in tf_idf_weights:
        graph.add_node(review_label, "review")

        for word, weight in weighted_terms:
            #Prefixo evita confundir palavra com nome de categoria ou review.
            word_label = "word:" + word
            graph.add_edge(
                review_label,
                word_label,
                weight,
                node_type_u="review",
                node_type_v="word",
            )

    for word_a, word_b, weight in pmi_edges:
        #PMI liga palavras nos dois sentidos.
        graph.add_edge(
            "word:" + word_a,
            "word:" + word_b,
            weight,
            node_type_u="word",
            node_type_v="word",
            bidirectional=True,
        )

    for seed, category in seed_pairs:
        #Seed ancora uma palavra em uma categoria conhecida.
        graph.add_edge(
            "word:" + seed,
            category,
            1.0,
            node_type_u="word",
            node_type_v="category",
        )

    return graph


def mock_documents():
    #Reviews pequenas para validar o fluxo antes do dataset real.
    return [
        ("R1", ["fps", "lag", "crash", "fps"]),
        ("R2", ["textura", "grafico", "resolucao", "visual"]),
        ("R3", ["controles", "gameplay", "diversao", "jogabilidade"]),
        ("R4", ["historia", "enredo", "personagem", "narrativa"]),
        ("R5", ["fps", "textura", "resolucao", "lag"]),
        ("R6", ["historia", "controles", "diversao", "enredo"]),
    ]


def mock_seed_groups():
    #Seeds escolhidas manualmente como exemplos de cada aspecto tecnico.
    return [
        ("Performance", ["fps", "lag", "crash", "stuttering"]),
        ("Graficos", ["textura", "resolucao", "grafico", "visual"]),
        ("Gameplay", ["controles", "gameplay", "diversao", "jogabilidade"]),
        ("Narrativa", ["historia", "enredo", "personagem", "narrativa"]),
    ]
