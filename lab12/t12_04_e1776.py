
class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:

    def __init__(self):
        self.top_node = None
        self._size = 0

    def push(self, n):
        new_node = Node(int(n))
        new_node.next = self.top_node
        self.top_node = new_node
        self._size += 1
        return "ok"

    def pop(self):
        if self.top_node is None:
            return "error"
        current_top = self.top_node
        item = current_top.item
        self.top_node = current_top.next
        self._size -= 1
        return item

    def back(self):
        if self.top_node is None:
            return "error"
        return self.top_node.item

    def size(self):
        return self._size



if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        vagons = list(range(1, n + 1))
        while True:
            arr = list(map(int, input().split()))
            if arr[0] == 0:
                break

            stack = Stack()
            i = 0
            for v in vagons:
                stack.push(v)
                while stack.size() > 0 and i < n and stack.back() == arr[i]:
                    stack.pop()
                    i += 1
            if i == n:
                print("Yes")
            else:
                print("No")
        print()
    print()



