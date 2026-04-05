
class Stack:

    def __init__(self, capacity=1000):
        self._items = [0 for _ in range(capacity)]
        self._index = 0

    def push(self, n):
        self._items[self._index] = n
        self._index += 1
        return "ok"

    def pop(self):
        el = self._items[self._index - 1]
        self._items[self._index - 1] = 0
        self._index -= 1
        return el

    def empty(self):
        return self._index == 0


def solve(num, base):
    stack = Stack()
    while num > 0:
        stack.push(num % base)
        num //= base
    conv = ''
    while not stack.empty():
        digit = stack.pop()
        if 0 <= digit < 10:
            conv += str(digit)
        else:
            conv += f'[{digit}]'
    return conv


if __name__ == '__main__':
    n = int(input())
    base = int(input())
    res = solve(n, base)
    print(res)
