from graph import Graph, Vertex, Edge


if __name__ == '__main__':
    g = Graph()
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)
    v5 = Vertex(5)
    v6 = Vertex(6)

    g.add_vertex(v1)
    g.add_vertex(v2)
    g.add_vertex(v3)
    g.add_vertex(v4)
    g.add_vertex(v5)
    g.add_vertex(v6)

    g.add_edge(Edge(v1, v2, 4))
    g.add_edge(Edge(v1, v3, 3))
    g.add_edge(Edge(v3, v4, 6))
    g.add_edge(Edge(v1, v4, 10))
    g.add_edge(Edge(v4, v5, 5))
    g.add_edge(Edge(v4, v6, 3))
    g.add_edge(Edge(v5, v6, 7))

    g_prime = g.dijkstra(1)

