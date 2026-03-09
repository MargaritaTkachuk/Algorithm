def bubble_sort(array):
    counter = 0
    n = len(array)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                counter += 1
    return counter

if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(bubble_sort(arr))