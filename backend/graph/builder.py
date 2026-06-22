#backend/graph/builder.py

from backend.graph.graph import Graph
from backend.graph.pmi import calculate_pmi
from backend.preprocessing.tf_idf import calculate_tf_idf


def _category_seed_pairs(seed_groups):
    pairs = []
    for category, seeds in seed_groups:
        for seed in seeds:
            #Transforma grupos em pares simples: palavra -> categoria.
            pairs.append((seed, category))
    return pairs


def build_tripartite_graph(documents, seed_groups, tf_idf_threshold=0.0, pmi_threshold=0.0):
    """
    Constroi o grafo tripartido:
    - review -> palavra com peso TF-IDF
    - palavra <-> palavra com peso PMI
    - palavra -> categoria com peso fixo de seed

    Tudo e representado em listas, sem bibliotecas prontas de grafo.
    """
    graph = Graph()
    #Pesos das tres familias de arestas do grafo.
    tf_idf_weights = calculate_tf_idf(documents, threshold=tf_idf_threshold)
    pmi_edges = calculate_pmi(documents, threshold=pmi_threshold)
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
    #Reviews pequenas simulando o output já lematizado do NLP.
    #Balanceado com 1 review por categoria para que o CMN não penalize desproporcionalmente.
    return [
        ("R1", ["fp", "lag", "crash", "trav"]),
        ("R2", ["text", "gráf", "resoluç", "visual"]),
        ("R3", ["control", "gameplay", "divers", "jogabil"]),
        ("R4", ["histór", "enred", "person", "narr"]),
    ]


def mock_seed_groups():
    return [
        ("Performance", ['fp', 'lag', 'crash', 'stuttering', 'trav', 'otimiz', 'desempenh', 'bug', 'qued', 'fram', 'gargal', 'pes', 'lev', 'rod', 'rod', 'lis', 'pc', 'rtx', 'gtx', 'process', 'plac', 'memor', 'ram', 'cpu', 'gpu', 'engin']),
        ("Gráfico", ['text', 'resoluç', 'gráf', 'visual', 'lind', 'fei', 'bel', 'sombr', 'ilumin', 'raytracing', 'pais', 'cen', 'real', 'fei', 'maravilh', '4k']),
        ("Gameplay", ['control', 'gameplay', 'divers', 'jogabil', 'mecân', 'jog', 'tir', 'dirig', 'miss', 'combat', 'loot', 'skill', 'habil', 'farm', 'grind', 'físic', 'mov', 'pul', 'tirotei', 'arm', 'carr', 'chef', 'bos', 'fas', 'level', 'dificuldad', 'flu', 'respond', 'roaming', 'assalt', 'roub', 'tuning', 'heist', 'onlin', 'vici', 'corr']),
        ("Narrativa", ['histór', 'enred', 'person', 'narr', 'campanh', 'final', 'lor', 'diálog', 'dubl', 'legend', 'traduç', 'emocion', 'vil', 'heró', 'plot', 'twist', 'rot', 'escrit', 'leit', 'livr']),
    ]
