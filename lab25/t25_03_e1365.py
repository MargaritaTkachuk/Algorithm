import sys
from queue import PriorityQueue

INF = sys.maxsize


class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.adj: list[dict] = [{} for _ in range(vertices)]

    def add_edge(self, source: int, destination: int, weight: int):
        self.adj[source][destination] = weight

    def dijkstra(self, start: int, end: int) -> int:
        distances = [INF] * self.vertices
        distances[start] = 0

        pq = PriorityQueue()
        pq.put((0, start))

        while not pq.empty():
            current_dist, u = pq.get()

            if current_dist > distances[u]:
                continue

            for v, weight in self.adj[u].items():
                new_dist = distances[u] + weight
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    pq.put((new_dist, v))

        return distances[end] if distances[end] < INF else -1


if __name__ == '__main__':
    first_line = input().split()
    n, s, f = int(first_line[0]), int(first_line[1]), int(first_line[2])

    g = Graph(n + 1)

    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(n):
            weight = row[j]
            if weight != -1 and i != j + 1:
                g.add_edge(i, j + 1, weight)

    print(g.dijkstra(s, f))