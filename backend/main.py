# backend/main.py
from graph import Graph

def main():
    print("Inicializando o Grafo Tripartido de Reviews...")
    g = Graph()
    
    # Exemplo de inserção de nós e arestas (Review -> Palavra)
    g.add_edge("r1_review_texto", "fps", 0.82)
    g.add_edge("r1_review_texto", "textura", 0.61)
    
    # Exemplo de inserção de arestas (Palavra -> Palavra)
    g.add_edge("fps", "lag", 0.74)
    g.add_edge("fps", "crash", 0.63)
    
    # Exemplo de inserção de arestas (Palavra -> Categoria)
    g.add_edge("fps", "Performance", 1.0)
    
    print("Vizinhos de 'fps':")
    print(g.get_neighbors("fps"))

if __name__ == "__main__":
    main()
