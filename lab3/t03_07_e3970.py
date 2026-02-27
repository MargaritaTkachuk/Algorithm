def binary_search(arr, x, n):
    l = 0
    r = n
    while l < r:
        m = l + (r - l) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return r


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    a = int(input())
    find = [int(x) for x in input().split()]
    for x in find:
        first_index = binary_search(arr, x, n)
        last_index = binary_search(arr, x + 1, n)
        print(last_index - first_index)


