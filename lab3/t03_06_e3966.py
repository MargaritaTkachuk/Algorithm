def binary_search(arr, x, n):
    l = 0
    r = n - 1
    while l < r:
        m = l + (r - l) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return arr[r] == x


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    a = int(input())
    find = [int(x) for x in input().split()]
    for x in find:
        if binary_search(arr, x, n):
            print('YES')
        else:
            print('NO')


