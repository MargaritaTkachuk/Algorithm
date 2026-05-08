

if __name__ == '__main__':
    n, m = map(int, input().split())
    deg_of_in = [0] * (n + 1)
    deg_of_out = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        deg_of_out[u] += 1
        deg_of_in[v] += 1
    for i in range(1, n + 1):
        print(deg_of_in[i], deg_of_out[i])