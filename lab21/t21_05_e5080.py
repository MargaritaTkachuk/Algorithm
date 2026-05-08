

if __name__ == '__main__':
    n = int(input())
    degrees = [0] * n
    for i in range(n):
        row = list(map(int, input().split()))
        degrees[i] = sum(row)
    count = 0
    for d in degrees:
        if d == 1:
            count += 1
    print(count)