def q_sort(array, left, right):
    if left >= right:
        return
    i = left
    j = right
    el = array[i + (j - i) // 2]
    while True:
        while array[i] < el:
            i += 1
        while array[j] > el:
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

if __name__ == '__main__':
    n = int(input())
    array = [int(x) for x in input().split()]
    quick_sort(array)
    print(*array)
