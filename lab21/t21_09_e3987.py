

if __name__ == '__main__':
    n, m = map(int, input().split())
    deg_of_v = [0] * (n + 1)
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        uv = [u, v]
        if uv in edges:
            continue
        deg_of_v[u] += 1
        deg_of_v[v] += 1
        edges.append(uv)
    for i in range(1, n + 1):
        if deg_of_v[i] != n - 1:
            print("NO")
            break
    else:
        print("YES")