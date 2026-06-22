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
    #Reviews pequenas simulando o output já lematizado do NLP.
    return [
        ("R1", ["fps", "lag", "crash", "fps"]),
        ("R2", ["textur", "grafic", "resoluca", "visual"]),
        ("R3", ["control", "gameplay", "divers", "jogabil"]),
        ("R4", ["histori", "enred", "personag", "narrativ"]),
        ("R5", ["fps", "textur", "resoluca", "lag"]),
        ("R6", ["histori", "control", "divers", "enred"]),
    ]


def mock_seed_groups():
    #Seeds massivamente expandidas com dezenas de gírias gamers e stems do RSLP
    return [
        ("Performance", ["fps", "lag", "crash", "stuttering", "trav", "otimiz", "desempenh", "bug", "queda", "frame", "gargal", "pesad", "lev", "roda", "rodou", "liso", "pc", "rtx", "gtx", "processador", "placa", "memoria", "ram", "cpu", "gpu"]),
        ("Graficos", ["textur", "resoluca", "grafic", "visual", "lind", "fei", "beleza", "art", "arte", "sombra", "iluminaca", "raytracing", "paisag", "cenari", "realist", "feio", "bonit", "maravilh"]),
        ("Gameplay", ["control", "gameplay", "divers", "jogabil", "mecani", "jogar", "tiro", "dirigir", "missa", "combat", "loot", "skill", "habilidad", "farm", "grind", "fisica", "moviment", "pul", "tirotei", "arma", "carr", "chef", "boss", "fase", "level", "dificuld"]),
        ("Narrativa", ["histori", "enred", "personag", "narrativ", "campanh", "fina", "lore", "dialog", "dublag", "legend", "tradu", "final", "emociona", "vila", "heroi", "plot", "twist", "roteir", "escrev", "leitur", "livr"]),
    ]
