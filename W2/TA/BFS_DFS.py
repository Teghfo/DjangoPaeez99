from collections import defaultdict, OrderedDict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        # self.graph = dict()

    def add_edge(self, u, v):
        # if u not in self.graph.keys():
        #     self.graph[u] = []
        # if v not in self.graph.keys():
        #     self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start_node):
        queue = []
        visited = len(self.graph) * [False]
        queue.append(start_node)
        visited[start_node] = True
        while queue:
            top_node = queue.pop(0)
            print(top_node, end=' ')
            for neighbor in self.graph[top_node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        print()

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_util(i, visited)

    def dfs(self, v):
        visited = [False] * len(self.graph)
        self.dfs_util(v, visited)

    def iterative_dfs(self, start_node):
        stack = []
        visited = len(self.graph)*[False]

        stack.append(start_node)
        while stack:
            top_node = stack.pop()
            if not visited[top_node]:
                print(top_node, end=' ')
                visited[top_node] = True
            for neighbor in self.graph[top_node][::-1]:
                if not visited[neighbor]:
                    stack.append(neighbor)



g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)
# g.bfs(0)
g.dfs(0)
g.iterative_dfs(0)