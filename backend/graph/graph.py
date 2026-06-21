# backend/graph/graph.py

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils import binary_search_tuples, sorted_insert_tuple


class Graph:
    def __init__(self):
        # Lista de adjacência: cada posição guarda os vizinhos daquele nó.
        self.adj = []

        # Índice -> rótulo legível do nó.
        self.labels = []

        # Tipo do nó usado pelo Label Propagation.
        self.node_types = []

        # Lista auxiliar ordenada alfabeticamente: [(label, idx), ...]
        # Permite busca binária O(log N) por rótulo, sem usar dict/hash.
        self.node_map = []

    def add_node(self, label: str, node_type: str = "unknown") -> int:
        """
        Adiciona um nó ao grafo se ele ainda não existir.
        A busca usa busca binária em node_map — O(log N) em vez de O(N).
        """
        idx = self._find_node_idx(label)
        if idx != -1:
            # Se o nó nasceu sem tipo, aproveitamos para completar depois.
            if self.node_types[idx] == "unknown" and node_type != "unknown":
                self.node_types[idx] = node_type
            return idx

        # O índice do nó será a posição dele nas três listas principais.
        new_idx = len(self.labels)
        self.labels.append(label)
        self.node_types.append(node_type)
        self.adj.append([])

        # Insere ordenado em node_map para permitir busca binária futura.
        sorted_insert_tuple(self.node_map, (label, new_idx))

        return new_idx

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

        # Aresta normal: review -> palavra ou palavra -> categoria.
        self._upsert_edge(u_idx, v_idx, weight)
        if bidirectional:
            # Aresta PMI: palavra <-> palavra.
            self._upsert_edge(v_idx, u_idx, weight)

    def _upsert_edge(self, u_idx: int, v_idx: int, weight: float):
        """
        Evita arestas duplicadas usando busca binária na lista de adjacência.
        Os vizinhos são mantidos ordenados pelo ID numérico — O(log N) busca.
        Se a aresta já existir, atualiza o peso.
        """
        neighbors = self.adj[u_idx]
        left = 0
        right = len(neighbors) - 1
        pos = len(neighbors)

        while left <= right:
            mid = (left + right) // 2
            neighbor_idx, _ = neighbors[mid]
            if neighbor_idx == v_idx:
                # Aresta já existe: apenas atualiza o peso.
                neighbors[mid] = (v_idx, weight)
                return
            elif neighbor_idx < v_idx:
                left = mid + 1
            else:
                pos = mid
                right = mid - 1

        # Aresta nova: insere na posição correta mantendo a ordem.
        neighbors.insert(pos, (v_idx, weight))

    def _find_node_idx(self, label: str) -> int:
        """
        Busca o índice do nó pela string usando busca binária em node_map.
        O(log N) em vez de O(N) com varredura linear.
        """
        map_pos = binary_search_tuples(self.node_map, label)
        if map_pos == -1:
            return -1
        return self.node_map[map_pos][1]

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