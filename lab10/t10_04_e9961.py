def solve(lst, n, k):
    if k == len(lst):
        print(*lst)
        return
    for i in range(1, n + 1):
        if i not in lst:
            solve(lst + [i], n, k)


if __name__ == '__main__':
    n, k = map(int, input().split())
    solve([], n, k)
