import heapq


class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n + 1)]

    def add_edge(self, u, v, w):
        self.adj[u].append((w, v))
        self.adj[v].append((w, u))

    def prim_mst(self):
        in_mst = [False] * (self.n + 1)
        mst_edges = set()
        heap = [(0, 1, -1)]

        while heap:
            w, v, u = heapq.heappop(heap)
            if in_mst[v]:
                continue
            in_mst[v] = True
            if u != -1:
                mst_edges.add(frozenset([u, v]))
            for w2, nb in self.adj[v]:
                if not in_mst[nb]:
                    heapq.heappush(heap, (w2, nb, v))

        return mst_edges

    def has_edge(self, p, q):
        for _, nb in self.adj[p]:
            if nb == q:
                return True
        return False

    def is_in_mst(self, p, q):
        if not self.has_edge(p, q):
            return False
        mst_edges = self.prim_mst()
        return frozenset([p, q]) in mst_edges


if __name__ == "__main__":

    with open("input.txt", "r") as f:
        lines = f.read().strip().split("\n")

        idx = 0
        t = int(lines[idx]); idx += 1

        for _ in range(t):
            n, m, p, q = map(int, lines[idx].split()); idx += 1
            graph = Graph(n)

            for _ in range(m):
                u, v, w = map(int, lines[idx].split()); idx += 1
                graph.add_edge(u, v, w)

            print("YES" if graph.is_in_mst(p, q) else "NO")