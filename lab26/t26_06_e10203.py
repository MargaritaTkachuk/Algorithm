import math
import heapq


class Graph:
    def __init__(self, coords):
        self.n = len(coords)
        self.xs = [c[0] for c in coords]
        self.ys = [c[1] for c in coords]

    def prim_mst_edges(self):
        n = self.n
        xs = self.xs
        ys = self.ys
        sqrt = math.sqrt
        INF = float('inf')

        in_mst = bytearray(n)
        min_d2 = [INF] * n
        parent = [-1] * n
        min_d2[0] = 0.0
        mst_weights = []

        for _ in range(n):
            best2 = INF
            v = 0
            for i in range(n):
                if not in_mst[i] and min_d2[i] < best2:
                    best2 = min_d2[i]
                    v = i
            in_mst[v] = 1
            if parent[v] != -1:
                mst_weights.append(sqrt(best2))
            vx = xs[v]
            vy = ys[v]
            for nb in range(n):
                if not in_mst[nb]:
                    dx = vx - xs[nb]
                    dy = vy - ys[nb]
                    d2 = dx * dx + dy * dy
                    if d2 < min_d2[nb]:
                        min_d2[nb] = d2
                        parent[nb] = v

        return mst_weights


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().strip().split("\n")

    idx = 0
    t = int(lines[idx]); idx += 1

    for _ in range(t):
        s, p = map(int, lines[idx].split()); idx += 1

        coords = []
        for i in range(p):
            x, y = map(int, lines[idx].split()); idx += 1
            coords.append((x, y))

        graph = Graph(coords)
        mst_weights = graph.prim_mst_edges()

        mst_weights.sort(reverse=True)
        d = mst_weights[s - 1] if s - 1 < len(mst_weights) else 0.0

        print(f"{d:.2f}")