def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        insertion = False
        el = array[i]
        pos = i
        while pos > 0:
            if array[pos - 1] > el:
                array[pos] = array[pos - 1]
                insertion = True
            else:
                break
            pos -= 1
        array[pos] = el
        if insertion:
            print(*array)

if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    insertion_sort(arr)
