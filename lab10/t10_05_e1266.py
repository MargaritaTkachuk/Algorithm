def q_sort(array, left, right):
    if left >= right:
        return
    i = left
    j = right
    el = array[i + (j - i) // 2]
    while True:
        while array[i] > el:
            i += 1
        while array[j] < el:
            j -= 1
        if i >= j:
            break
        array[i], array[j] = array[j], array[i]

        i += 1
        j -= 1
    q_sort(array, left, j)
    q_sort(array, j + 1, right)

def quick_sort(array):
    left = 0
    right = len(array) - 1
    q_sort(array, left, right)


def solve(n, lst, res, i, current_max):
    if current_max[0] == n:
        return current_max[0]

    if i == len(lst):
        if res > current_max[0]:
            current_max[0] = res
        return res

    if res + sum(lst[i:]) <= current_max[0]:
        return current_max[0]

    if res + lst[i] <= n:
        solve(n, lst, res + lst[i], i + 1, current_max)

    solve(n, lst, res, i + 1, current_max)

    return current_max[0]


if __name__ == '__main__':
    f = open("input.txt")
    for line in f:
        data = [int(x) for x in line.split()]
        N = data[0]
        s = data[1]
        tracks = data[2:]
        quick_sort(tracks)
        best = [0]
        print('sum:' + str(solve(N, tracks, 0, 0, best)))
    f.close()