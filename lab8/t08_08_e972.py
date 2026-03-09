def selection_sort(array):
    n = len(array)
    for i in range(n - 1, 0, -1):
        max_index = 0
        for j in range(1, i + 1):
            if array[max_index] < array[j]:
                max_index = j
        array[j], array[max_index] = array[max_index], array[j]

if __name__ == '__main__':
    n = int(input())
    data = []
    for _ in range(n):
        lst = [int(x) for x in input().split()]
        data.append(lst)
    selection_sort(data)
    for t in data:
        print(*t)