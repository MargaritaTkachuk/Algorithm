from collections import deque

class Graph:
    def __init__(self, n):
        self.vertices = {
            i: set() for i in range(1, n + 1)
        }

    def add_edge(self, u, v):
        self.vertices[u].add(v)
        self.vertices[v].add(u)

    def last(self, burned):
        queue = deque()
        dist = {}
        for v in burned:
            queue.append(v)
            dist[v] = 0
        while queue:
            vertex = queue.popleft()
            for neighbour in self.vertices[vertex]:
                if neighbour not in dist:
                    dist[neighbour] = dist[vertex] + 1
                    queue.append(neighbour)
        last_vertex = -1
        max_time = -1
        for v in dist:
            if dist[v] > max_time:
                max_time = dist[v]
                last_vertex = v
            elif dist[v] == max_time and v < last_vertex:
                last_vertex = v
        return max_time, last_vertex


if __name__ == '__main__':
    f = open("input.txt")
    n, m = map(int, f.readline().split())
    graph = Graph(n)
    for _ in range(m):
        u, v = map(int, f.readline().split())
        graph.add_edge(u, v)
    k = int(f.readline())
    burned = list(map(int, f.readline().split()))
    t, v = graph.last(burned)
    print(t)
    print(v)
    f.close()