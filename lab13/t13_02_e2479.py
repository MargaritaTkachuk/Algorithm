
BRACKETS = {
    ")" : "(", "]" : "["
}

def solve(s):
    stack = []
    for b in BRACKETS.values():
        stack.append(b)
    else:
        if len(stack) == 0:
            return False
        if stack.pop() != BRACKETS[b]:
            return False
    return len(stack) == 0


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        arr = [str(e) for e in input().strip()]
        res = solve(arr)
        if res:
            print("Yes")
        else:
            print("No")