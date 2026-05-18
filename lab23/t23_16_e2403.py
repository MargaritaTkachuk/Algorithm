import sys
sys.setrecursionlimit(100000)


class Graph:
    def __init__(self, n):
        self.vertices = {
            i: set() for i in range(1, n + 1)
        }
        self.n = n

    def add_edge(self, u, v):
        self.vertices[u].add(v)

    def dfs(self, v, used, graph, order = None):
        used[v] = True
        for to in graph[v]:
            if not used[to]:
                self.dfs(to, used, graph, order)
        if order is not None:
            order.append(v)

    def transpose(self):
        transposed = {
            v: [] for v in self.vertices
        }
        for u in self.vertices:
            for v in self.vertices[u]:
                transposed[v].append(u)
        return transposed

    def kosaraju(self):
        used = [False] * (self.n + 1)
        order = []
        for v in range(1, self.n + 1):
            if not used[v]:
                self.dfs(v, used, self.vertices, order)
        transposed = self.transpose()
        used = [False] * (self.n + 1)
        components = 0
        while order:
            v = order.pop()
            if not used[v]:
                self.dfs(v, used, transposed)
                components += 1
        return components


if __name__ == '__main__':
    f = open("input.txt")
    n, m = map(int, f.readline().split())
    graph = Graph(n)
    for _ in range(m):
        u, v = map(int, f.readline().split())
        graph.add_edge(u, v)
    component = graph.kosaraju()
    print(component)
    f.close()