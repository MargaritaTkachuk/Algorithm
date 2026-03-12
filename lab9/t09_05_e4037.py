def merge_sort(array):
    if len(array) <= 1:
        return

    m = len(array) // 2
    arr_left = array[:m]
    arr_right = array[m:]

    merge_sort(arr_left)
    merge_sort(arr_right)

    i = j = k = 0

    while i < len(arr_left) and j < len(arr_right):
        if arr_left[i][0] <= arr_right[j][0]:
            array[k] = arr_left[i]
            i += 1
        else:
            array[k] = arr_right[j]
            j += 1
        k += 1

    while i < len(arr_left):
        array[k] = arr_left[i]
        i += 1
        k += 1

    while j < len(arr_right):
        array[k] = arr_right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    n = int(input())
    array = []

    for _ in range(n):
        lst = list(map(int, input().split()))
        array.append(lst)

    merge_sort(array)

    for l in array:
        print(*l)