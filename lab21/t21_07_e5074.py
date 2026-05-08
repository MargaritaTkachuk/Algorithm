

if __name__ == '__main__':
    n, m = map(int, input().split())
    deg_of_v = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        deg_of_v[u] += 1
        deg_of_v[v] += 1
    for i in range(1, n + 1):
        print(deg_of_v[i])