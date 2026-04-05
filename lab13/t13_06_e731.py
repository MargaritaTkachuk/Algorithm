class Stack:

    def __init__(self, capacity=100):
        self._items = [None for _ in range(capacity)]
        self._index = 0

    def push(self, n):
        self._items[self._index] = n
        self._index += 1

    def pop(self):
        self._index -= 1
        return self._items[self._index]


def priority(op):
    if op in "+-":
        return 1
    if op in "*/":
        return 2
    return 3


def solve(expr):
    stack = Stack()

    for el in reversed(expr):
        if el.isalpha():
            stack.push((el, 3))
        else:
            left, p1 = stack.pop()
            right, p2 = stack.pop()

            p = priority(el)

            if p1 < p:
                left = f"({left})"
            if p2 < p or (el in "-/" and p2 == p):
                right = f"({right})"

            new_expr = left + el + right
            stack.push((new_expr, p))

    return stack.pop()[0]


if __name__ == '__main__':
    expr = input().strip()
    print(solve(expr))