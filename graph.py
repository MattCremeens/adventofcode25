import numpy as np
import copy


class SparseMatrix:
    def __init__(self):
        self.data = {}  # row → {col: value}

    def __getitem__(self, idx):
        i, j = idx
        return self.data.get(i, {}).get(j, None)

    def __setitem__(self, idx, value):
        i, j = idx
        self.data.setdefault(i, {})[j] = value

    def remove(self, i, j):
        """
        Removes the entry at (i, j).
        If the row becomes empty, remove the row as well.
        Silently does nothing if the entry does not exist.
        """
        row = self.data.get(i)
        if row is None:
            return  # nothing to remove

        row.pop(j, None)  # remove column entry if present

        # If row-dict is now empty, remove the row entirely
        if not row:
            del self.data[i]

    def pop(self, i, j, default=None):
        """
        Removes and returns the value at (i,j).
        Returns default if not found.
        """
        row = self.data.get(i)
        if row is None:
            return default

        value = row.pop(j, default)

        if not row:
            del self.data[i]

        return value

    def items(self):
        """Iterate over ((row, col), value) pairs."""
        for i, row in self.data.items():
            for j, value in row.items():
                yield (i, j), value

    def min_entry(self, include_cols=None):
        """
        Returns (row, col, value) of the minimum stored entry.
        include_cols: optional set/list of column indices to consider.
        Ties are broken arbitrarily.
        Raises ValueError if no entries remain after filtering.
        """
        include_cols = None if include_cols is None else set(include_cols)

        min_row = min_col = None
        min_val = None

        for (i, j), value in self.items():
            if include_cols is not None and j not in include_cols:
                continue
            if min_val is None or value < min_val:
                min_row, min_col, min_val = i, j, value

        if min_val is None:
            raise ValueError("No entries found in the specified columns")

        return min_row, min_col, min_val

class Vertex:
    def __init__(self, id, data=None):
        """
        id   – unique identifier (string, int, etc.)
        data – optional payload stored in the vertex
        """
        self.id = id
        self.data = data

    def __repr__(self):
        return f"Vertex(id={self.id}, data={self.data})"


class Edge:
    def __init__(self, source, target, weight=1, directed=False, data=None):
        """
        source, target – Vertex objects
        weight         – numerical weight
        directed       – whether this edge is directed
        data           – optional payload stored in the edge
        """
        self.source = source
        self.target = target
        self.weight = weight
        self.directed = directed
        self.data = data

    def __repr__(self):
        direction = "->" if self.directed else "--"
        return f"Edge({self.source.id} {direction} {self.target.id}, weight={self.weight})"


class Graph:
    def __init__(self):
        # Store vertices by their ID for quick lookups
        self.vertices = {}
        # Adjacency list: id -> list of Edge objects
        self.adjacency = {}

    def add_vertex(self, vertex):
        """Add a Vertex object to the graph."""
        if vertex.id in self.vertices:
            raise ValueError(f"Vertex '{vertex.id}' already exists.")
        self.vertices[vertex.id] = vertex
        self.adjacency[vertex.id] = []

    def add_edge(self, edge):
        """Add an Edge object to the graph and update adjacency lists."""
        if edge.source.id not in self.vertices or edge.target.id not in self.vertices:
            raise ValueError("Both vertices must exist before adding an edge.")

        # Add to adjacency list
        self.adjacency[edge.source.id].append(edge)

        # If undirected, add reverse edge
        if not edge.directed:
            reverse = Edge(edge.target, edge.source, weight=edge.weight, directed=False, data=edge.data)
            self.adjacency[edge.target.id].append(reverse)

    def get_neighbors(self, vertex_id):
        """Return list of (neighbor_vertex, edge) pairs."""
        if vertex_id not in self.vertices.keys():
            raise ValueError(f"Vertex {vertex_id} does not exist. Must be one of {self.vertices.keys()}")
        return [(edge.target, edge) for edge in self.adjacency[vertex_id]]

    @property
    def num_vertices(self):
        return len(self.vertices)

    def __repr__(self):
        return f"Graph(vertices={len(self.vertices)}, edges={sum(len(v) for v in self.adjacency.values())})"

    def dijkstra(self, start_id):
        Q = copy.deepcopy(self.vertices)
        d = SparseMatrix()
        p = np.empty(self.num_vertices+1, dtype=object)
        delta = SparseMatrix()
        for v in self.vertices.values():
            if v.id != start_id:
                d[start_id, v.id] = 1e6
            else:
                d[start_id, v.id] = 0
        while len(Q) != 0:
            row, col, min_val = d.min_entry(list(Q))
            v = self.vertices[col]
            Q.pop(col)
            for v_prime in self.get_neighbors(v.id):
                delta[start_id, v_prime[0].id] = d[start_id, v.id] + v_prime[1].weight
                if delta[start_id, v_prime[0].id] < d[start_id, v_prime[0].id]:
                    d[start_id, v_prime[0].id] = delta[start_id, v_prime[0].id]
                    p[v_prime[0].id] = v

        v_prime = copy.deepcopy(self.vertices)
        output_graph = Graph()
        for i in range(1, 7):
            output_graph.add_vertex(Vertex(i))
        output_graph.vertices = copy.deepcopy(v_prime)
        for v in self.vertices.values():
            if p[v.id] is not None:
                output_graph.add_edge(Edge(v, p[v.id]))
        print(output_graph)
        return output_graph
