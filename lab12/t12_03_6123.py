class Stack:

    def __init__(self, capacity = 100):
        self._items = [0 for _ in range(capacity)]
        self._index = 0

    def push(self, n):
        self._items[self._index] = n
        self._index += 1
        return "ok"

    def pop(self):
        if self._index == 0:
            return "error"
        el = self._items[self._index - 1]
        self._items[self._index - 1] = 0
        self._index -= 1
        return el

    def back(self):
        if self._index == 0:
            return "error"
        return self._items[self._index - 1]

    def size(self):
        return self._index

    def clear(self):
        self.__init__(len(self._items))
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    f = open("input.txt")
    stack = Stack()
    for line in f:
        result = stack.execute(line)
        print(result)
        if result == "bye":
            break

    f.close()