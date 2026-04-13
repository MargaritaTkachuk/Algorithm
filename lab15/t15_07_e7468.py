class Node:

    def __init__(self, data: int):
        self.data: int = data
        self.next: [Node | None] = None
        self.prev: [Node | None] = None

class List:

    def __init__(self):
        self.head: [Node | None] = None
        self.tail: [Node | None] = None

    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def ReorderList(self) -> None:
        if self.head is None or self.head == self.tail:
            return
        left = self.head
        right = self.tail
        while left and right and left != right and left.prev != right:
            next_left = left.next
            prev_right = right.prev
            left.next = right
            right.prev = left
            if next_left != right:
                right.next = next_left
                next_left.prev = right
            else:
                right.next = None
            left = next_left
            right = prev_right
        if left:
            left.next = None
            self.tail = left

    def Print(self) -> None:
        item = self.head
        while item is not None:
            print(item.data, end=" ")
            item = item.next



if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    lst = List()
    for i in arr:
        lst.addToTail(i)
    lst.ReorderList()
    lst.Print()
