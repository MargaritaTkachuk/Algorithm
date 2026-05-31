import sys

INF = sys.maxsize


class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.dist: list[list[int]] = [[INF] * vertices for _ in range(vertices)]

    def set_edge(self, i: int, j: int, weight: int):
        self.dist[i][j] = weight

    def floyd_warshall(self) -> list[list[int]]:
        n = self.vertices

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.dist[i][k] != INF and self.dist[k][j] != INF:
                        if self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
                            self.dist[i][j] = self.dist[i][k] + self.dist[k][j]

        return self.dist


if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    idx = 0

    n = int(input_data[idx]); idx += 1

    g = Graph(n)

    for i in range(n):
        for j in range(n):
            w = int(input_data[idx]); idx += 1
            g.set_edge(i, j, w)

    result = g.floyd_warshall()

    for row in result:
        print(*row)