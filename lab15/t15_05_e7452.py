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

    def Print(self) -> None:
        # item = self.head
        # elements = []
        # while item is not None:
        #     elements.append(item.data)
        #     item = item.next
        # return elements
        item = self.head
        while item is not None:
            print(item.data, end=" ")
            item = item.next
        print()

    def PrintReverse(self) -> None:
        # elements = self.Print()
        # return elements[::-1]
        item = self.tail
        while item is not None:
            print(item.data, end=" ")
            item = item.prev
        print()


if __name__ == '__main__':
    n = int(input())
    inp = [int(el) for el in input().split()]
    lst = List()
    for el in inp:
        lst.addToTail(el)
    lst.Print()
    lst.PrintReverse()

