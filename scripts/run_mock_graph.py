# scripts/run_mock_graph.py

import sys
from pathlib import Path


if __package__ is None or __package__ == "":
    # Permite rodar com: uv run python scripts/run_mock_graph.py
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from backend.graph.builder import build_tripartite_graph, mock_documents, mock_seed_groups
from backend.propagation.label_propagation import classify_reviews, label_propagation


def main():
    print("Inicializando o Grafo Tripartido de Reviews...")

    #Pipeline completa usando dados mockados.
    graph = build_tripartite_graph(mock_documents(), mock_seed_groups())
    scores = label_propagation(graph, iterations=30, threshold=0.0001)
    classifications = classify_reviews(graph, scores)

    print("\nNos:", graph.size())
    print("\nClassificacoes mockadas:")
    for review_label, category, score, all_scores, top_words in classifications:
        #Mostra a melhor categoria e tambem o vetor completo de scores.
        print(f"- {review_label}: {category} ({score:.3f})")
        print(f"  scores: {all_scores}")
        print(f"  top_words: {top_words}")

    print("\nVizinhos de word:fps:")
    print(graph.get_neighbors("word:fps"))


if __name__ == "__main__":
    main()
