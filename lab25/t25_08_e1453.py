import sys

INF = 30000


class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.edges: list[tuple] = []

    def add_edge(self, source: int, destination: int, weight: int):
        self.edges.append((source, destination, weight))

    def bellman_ford(self, start: int) -> list[int]:
        distances = [INF] * (self.vertices + 1)
        distances[start] = 0

        for _ in range(self.vertices - 1):
            relaxed = False
            for u, v, weight in self.edges:
                if distances[u] != INF and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    relaxed = True
            if not relaxed:
                break

        return distances[1:]


if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    idx = 0

    n, m = int(input_data[idx]), int(input_data[idx + 1])
    idx += 2

    g = Graph(n)

    for _ in range(m):
        u, v, w = int(input_data[idx]), int(input_data[idx + 1]), int(input_data[idx + 2])
        idx += 3
        g.add_edge(u, v, w)

    print(*g.bellman_ford(1))