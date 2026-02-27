def binary(n):
    res = ''
    while n > 0:
        res += str(n % 2)
        n //= 2
    return res[::-1]

def decimal(line):
    n = line[::-1]
    res = 0
    for i in range(len(n)):
        res += 2**i * int(n[i])
    return res

def gen_arr(line):
    arr = []
    temp = line
    for i in range(len(line)):
        temp = temp[1:] + temp[0]
        arr.append(decimal(temp))
    return arr

def find_max(arr):
    maxim = arr[0]
    for el in arr:
        if el > maxim:
            maxim = el
    return maxim

if __name__ == '__main__':
    n = int(input())
    n1 = binary(n)
    arr = gen_arr(n1)
    print(find_max(arr))