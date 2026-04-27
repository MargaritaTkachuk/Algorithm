

def is_heap(arr):
    n = len(arr)
    for i in range(n):
        if 2 * i + 1 < n and arr[i] > arr[2 * i + 1]:
                return False
        if 2 * i + 2 < n and arr[i] > arr[2 * i + 2]:
                return False
    return True


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    val = is_heap(arr)
    if val:
        print("YES")
    else:
        print("NO")

