from collections import deque

class Graph:
    def __init__(self, n):
        self.vertices = {
            i: set() for i in range(1, n + 1)
        }

    def add_edge(self, u, v):
        self.vertices[u].add(v)
        #self.vertices[v].add(u)

    def count_paths(self, start, finish, d):
        count = 0
        stack = [
            (start, [start], 0)
        ]
        while stack:
            vertex, path, depth = stack.pop()
            if depth > d:
                continue
            if vertex == finish:
                count += 1
                continue
            for neighbour in self.vertices[vertex]:
                if neighbour not in path:
                    stack.append(
                        (neighbour,
                        path + [neighbour],
                        depth + 1)
                    )
        return count


if __name__ == '__main__':
    f = open("input.txt")
    n, k, a, b, d = map(int, f.readline().split())
    graph = Graph(n)
    for _ in range(k):
        u, v = map(int, f.readline().split())
        graph.add_edge(u, v)
    paths = graph.count_paths(a, b, d)
    print(paths)
    f.close()