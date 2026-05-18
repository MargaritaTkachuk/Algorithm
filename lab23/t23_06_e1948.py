import sys
sys.setrecursionlimit(100000)

class CycleError(Exception):
    pass

class Graph:
    def __init__(self, n):
        self.vertices = {
            i: set() for i in range(1, n + 1)
        }
        self.colors = {i: 'white' for i in range(1, n + 1)}

    def add_edge(self, u, v):
        self.vertices[u].add(v)

    def dfs(self, visited, start):
        if self.colors[start] == 'black':
            return
        if self.colors[start] == 'grey':
            raise CycleError
        self.colors[start] = 'grey'
        for neighbour in self.vertices[start]:
                self.dfs(visited, neighbour)
        self.colors[start] = 'black'
        visited.append(start)

    def topological(self):
        try:
            visited = []
            for vertex in self.vertices:
                self.dfs(visited, vertex)
            sequence = []
            while visited:
                sequence.append(visited.pop())
            return sequence
        except CycleError:
            return [-1]

if __name__ == '__main__':
    f = open("input.txt")
    n, m = map(int, f.readline().split())
    graph = Graph(n)
    for _ in range(m):
        u, v = map(int, f.readline().split())
        graph.add_edge(u, v)
    top = graph.topological()
    print(*top)
    f.close()