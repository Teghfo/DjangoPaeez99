class Graph:
    """
    simple graph
    """

    def __init__(self):
        self.adjList = {}

    def add_node(self, node_a):
        self.adjList[node_a] = []

    def add_edge(self, node_a, node_b):
        if node_a not in self.adjList.keys():
            self.add_node(node_a)

        if node_b not in self.adjList.keys():
            self.add_node(node_b)
        if node_b not in self.adjList[node_a]:
            self.adjList[node_a].append(node_b)
        if node_a not in self.adjList[node_b]:
            self.adjList[node_b].append(node_a)

    def print_graph(self):
        print(self.adjList)

    def short_path(self, node_a, node_b):
        pass

    def is_connencted(self):
        pass

    def find_all_paths(self, start_node, end_node, path=[]):
        path = path + [start_node]
        if start_node == end_node:
            return [path]
        paths = []
        for node in self.adjList[start_node]:
            if node not in path:
                temp_paths = self.find_all_paths(node,
                                                 end_node,
                                                 path)
                for item in temp_paths:
                    paths.append(item)
        return paths

    def find_path(self, start_node, end_node, path=[]):
        path = path + [start_node]
        print(path)
        if start_node == end_node:
            return path

        for node in self.adjList[start_node]:
            if node not in path:
                temp_path = self.find_path(node, end_node, path)

                if temp_path:
                    return temp_path


g = Graph()
g.add_node("a")
g.add_node("b")
g.add_node("c")
g.add_node("d")
g.add_node("e")
g.add_node("m")
g.add_node("f")


g.add_edge("a", "c")
g.add_edge("b", "c")
g.add_edge("a", "b")
g.add_edge("d", "e")
g.add_edge("e", "c")
g.add_edge("a", "d")
g.add_edge("e", "m")
g.add_edge("d", "f")


# g.print_graph()

# print(g.find_path("a", "f"))
print(sorted(g.find_all_paths("a", "b"), key=len)[0])


print(g.find_all_paths("a", "b"))
