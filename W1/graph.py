class Graph:
    """
    simple graph
    """

    def __init__(self):
        self.edges = {}

    def add_node(self, node_a):
        self.edges[node_a] = []

    def add_edge(self, node_a, node_b):
        if node_a not in self.edges.keys():
            self.add_node(node_a)

        if node_b not in self.edges.keys():
            self.add_node(node_b)
        if node_b not in self.edges[node_a]:
            self.edges[node_a].append(node_b)
        if node_a not in self.edges[node_b]:
            self.edges[node_b].append(node_a)

    def print_graph(self):
        print(self.edges)

    def short_path(self, node_a, node_b):
        pass

    def is_connencted(self):
        pass


g = Graph()
g.add_node("a")
g.add_node("b")
g.add_node("c")
g.add_node("d")
g.add_node("e")


g.add_edge("a", "b")
g.add_edge("a", "c")
g.add_edge("d", "e")
g.add_edge("e", "c")


g.print_graph()
