from math import ceil


def time_exhaustion(arr, m, k):
    radiator_time = m
    for el in arr:
        if el > m:
            radiator_time -= ceil((el - m ) / (k - 1))
    return radiator_time < 0


def solve(arr, k):
    l = 1
    r = max(arr)
    while l < r:
        m = l + (r - l) // 2
        if time_exhaustion(arr, m, k):
            l = m + 1
        else:
            r = m
    return r


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    if k == 1:
        print(max(arr))
    else:
        print(solve(arr, k))
