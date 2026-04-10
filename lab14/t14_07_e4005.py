
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
    n = int(input())
    first = [int(card) for card in input().split()]
    second = [int(card) for card in input().split()]
    q_first = Queue()
    q_second = Queue()
    for card in first:
        q_first.push(card)
    for card in second:
        q_second.push(card)
    go = 0
    while not q_first.empty() and not q_second.empty() and go < 200000:
        card_1 = q_first.pop()
        card_2 = q_second.pop()
        if card_1 == 0 and card_2 == n - 1:
            q_first.push(0)
            q_first.push(n - 1)
        elif card_1 == n - 1 and card_2 == 0:
            q_second.push(n - 1)
            q_second.push(0)
        else:
            if card_1 > card_2:
                q_first.push(card_1)
                q_first.push(card_2)
            else:
                q_second.push(card_1)
                q_second.push(card_2)
        go += 1
    if q_first.empty():
        print(f'second {go}')
    elif q_second.empty():
        print(f'first {go}')
    else:
        print('draw')



