#backend/graph/graph.py


class Graph:
    def __init__(self):
        #Lista de adjacencia: cada posicao guarda os vizinhos daquele no.
        self.adj = []

        #Indice -> rotulo legivel do no.
        self.labels = []

        #Tipo do no usado pelo Label Propagation.
        self.node_types = []

    def add_node(self, label: str, node_type: str = "unknown") -> int:
        """
        Adiciona um no ao grafo se ele ainda nao existir.
        A busca usa apenas lista, sem dict/set/hash table.
        """
        idx = self._find_node_idx(label)
        if idx != -1:
            #Se o no nasceu sem tipo, aproveitamos para completar depois.
            if self.node_types[idx] == "unknown" and node_type != "unknown":
                self.node_types[idx] = node_type
            return idx

        #O indice do no sera a posicao dele nas tres listas.
        self.labels.append(label)
        self.node_types.append(node_type)
        self.adj.append([])
        return len(self.labels) - 1

    def add_edge(
        self,
        label_u: str,
        label_v: str,
        weight: float,
        node_type_u: str = "unknown",
        node_type_v: str = "unknown",
        bidirectional: bool = False,
    ):
        """Adiciona uma aresta ponderada. Use bidirectional=True para P <-> P."""
        u_idx = self.add_node(label_u, node_type_u)
        v_idx = self.add_node(label_v, node_type_v)

        #Aresta normal: review -> palavra ou palavra -> categoria.
        self._upsert_edge(u_idx, v_idx, weight)
        if bidirectional:
            #Aresta PMI: palavra <-> palavra.
            self._upsert_edge(v_idx, u_idx, weight)

    def _upsert_edge(self, u_idx: int, v_idx: int, weight: float):
        """
        Evita arestas duplicadas usando varredura linear na lista de adjacencia.
        Se a aresta ja existir, atualiza o peso.
        """
        for i in range(len(self.adj[u_idx])):
            neighbor_idx, _ = self.adj[u_idx][i]
            if neighbor_idx == v_idx:
                #Atualiza em vez de duplicar a mesma conexao.
                self.adj[u_idx][i] = (v_idx, weight)
                return
        self.adj[u_idx].append((v_idx, weight))

    def _find_node_idx(self, label: str) -> int:
        """Busca o indice do no pela string, sem tabela hash."""
        for i in range(len(self.labels)):
            if self.labels[i] == label:
                return i
        return -1

    def get_neighbors(self, label: str):
        idx = self._find_node_idx(label)
        if idx == -1:
            return []

        return [(self.labels[v_idx], weight) for v_idx, weight in self.adj[idx]]

    def get_neighbors_by_idx(self, idx: int):
        if idx < 0 or idx >= len(self.adj):
            return []
        return self.adj[idx]

    def get_node_type(self, label: str) -> str:
        idx = self._find_node_idx(label)
        if idx == -1:
            return ""
        return self.node_types[idx]

    def size(self) -> int:
        return len(self.labels)
