#backend/main.py

try:
    from .graph_builder import build_tripartite_graph, mock_documents, mock_seed_groups
    from .label_propagation import classify_reviews, label_propagation
except ImportError:
    from graph_builder import build_tripartite_graph, mock_documents, mock_seed_groups
    from label_propagation import classify_reviews, label_propagation


def main():
    print("Inicializando o Grafo Tripartido de Reviews...")

    #Pipeline completa usando dados mockados.
    graph = build_tripartite_graph(mock_documents(), mock_seed_groups())
    scores = label_propagation(graph, iterations=30, threshold=0.0001)
    classifications = classify_reviews(graph, scores)

    print("\nNos:", graph.size())
    print("\nClassificacoes mockadas:")
    for review_label, category, score, all_scores in classifications:
        #Mostra a melhor categoria e tambem o vetor completo de scores.
        print(f"- {review_label}: {category} ({score:.3f})")
        print(f"  scores: {all_scores}")

    print("\nVizinhos de word:fps:")
    print(graph.get_neighbors("word:fps"))


if __name__ == "__main__":
    main()
