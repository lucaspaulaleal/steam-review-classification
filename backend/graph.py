# backend/graph.py

class Graph:
    def __init__(self):
        # Arestas representadas por uma lista de listas:
        # self.adj[i] contém uma lista de tuplas (vizinho_idx, peso)
        self.adj = []
        
        # Mapeamento de índice para rótulo (ex: 0 -> "Review1", 1 -> "fps")
        self.labels = []

    def add_node(self, label: str) -> int:
        """
        Adiciona um nó ao grafo se ele não existir.
        Como não podemos usar dict/hash tables, faremos uma busca linear ou binária na lista.
        Para simplificar no boilerplate, busca linear, mas idealmente manter ordenado.
        """
        idx = self._find_node_idx(label)
        if idx != -1:
            return idx
        
        self.labels.append(label)
        self.adj.append([])
        return len(self.labels) - 1

    def add_edge(self, label_u: str, label_v: str, weight: float):
        """Adiciona uma aresta ponderada entre u e v."""
        u_idx = self.add_node(label_u)
        v_idx = self.add_node(label_v)
        
        self.adj[u_idx].append((v_idx, weight))
        # Se for grafo não direcionado, descomentar a linha abaixo
        # self.adj[v_idx].append((u_idx, weight))

    def _find_node_idx(self, label: str) -> int:
        """
        Busca o índice do nó pela string (label).
        Sem usar tabela hash (dict), iteramos sobre a lista.
        Obs: Para otimização futura, manter self.labels ordenado
        e usar busca binária (O(log N)).
        """
        for i in range(len(self.labels)):
            if self.labels[i] == label:
                return i
        return -1

    def get_neighbors(self, label: str):
        idx = self._find_node_idx(label)
        if idx == -1:
            return []
        
        # Retorna lista de vizinhos com os rótulos em vez de índices
        return [(self.labels[v_idx], weight) for v_idx, weight in self.adj[idx]]
