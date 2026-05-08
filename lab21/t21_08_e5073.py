

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    yes = False
    for _ in range(m):
        uv = [int(x) for x in input().split()]
        if uv in edges:
            print("YES")
            yes = True
            break
        edges.append(uv)
    if not yes:
        print("NO")


