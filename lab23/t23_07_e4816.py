import sys
sys.setrecursionlimit(1000000)


class Graph:
    def __init__(self, n):
        self.vertices = {
            i: [] for i in range(1, n + 1)
        }

    def add_edge(self, u, v):
        self.vertices[u].append(v)
        self.vertices[v].append(u)

    def dfs(self, v, used, comp):

        used[v] = True
        comp.append(v)

        for to in self.vertices[v]:
            if not used[to]:
                self.dfs(to, used, comp)

    def find_components(self):

        used = [False] * (len(self.vertices) + 1)

        components = []

        for v in self.vertices:

            if not used[v]:

                comp = []

                self.dfs(v, used, comp)

                components.append(comp)

        return components


if __name__ == '__main__':

    f = open("input.txt")

    n, m = map(int, f.readline().split())

    graph = Graph(n)

    for _ in range(m):
        u, v = map(int, f.readline().split())
        graph.add_edge(u, v)

    components = graph.find_components()

    print(len(components))

    for comp in components:
        print(len(comp))
        print(*comp)

    f.close()