
class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:

    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def empty(self):
        return self._front is None and self._back is None

    def push(self, n):
        new_node = Node(int(n))
        if self.empty():
            self._front = new_node
        else:
            self._back.next = new_node
        self._back = new_node
        self._size += 1
        return "ok"

    def pop(self):
        if self.empty():
            return "error"
        current_front = self._front
        item = current_front.item
        self._front = self._front.next
        if self._front is None:
            self._back = None
        self._size -= 1
        return item

    def front(self):
        if self.empty():
            return "error"
        return self._front.item

    def size(self):
        return self._size

    def clear(self):
        self._front = None
        self._back = None
        self._size = 0
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    f = open("input.txt")
    stack = Queue()
    for line in f:
        result = stack.execute(line)
        print(result)
        if result == "bye":
            break

    f.close()

