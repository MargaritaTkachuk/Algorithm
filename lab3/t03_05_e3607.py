import sys
input = sys.stdin.readline

def solve(arr, a, b):
    counter = 0
    for num in arr:
        if a <= num <= b:
            counter += 1
    return counter


if __name__ == '__main__':
    with open("input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            n = int(line)
            arr = map(int, f.readline().split())
            a, b = map(int, f.readline().split())
            print(solve(arr, a, b))
