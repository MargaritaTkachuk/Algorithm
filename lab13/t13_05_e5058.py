BRACKETS = {
    ")": "(",
    "]": "[",
    "}": "{"
}

def solve(s):
    stack = []
    for b in s:
        if b in BRACKETS.values():
            stack.append(b)
        elif b in BRACKETS:
            if len(stack) == 0:
                return False
            if stack.pop() != BRACKETS[b]:
                return False
    return len(stack) == 0


if __name__ == '__main__':
    arr = input().strip()
    res = solve(arr)
    if res:
        print("yes")
    else:
        print("no")