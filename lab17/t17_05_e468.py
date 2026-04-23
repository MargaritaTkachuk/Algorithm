class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self,key):
        if key < self.key:
            if self.left is None:
                self.left = BinaryTree(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = BinaryTree(key)
            else:
                self.right.insert(key)

    def find(self, key):
        if self.key == key:
            return self
        elif key < self.key and self.left is not None:
            return self.left.find(key)
        elif key > self.key and self.right is not None:
            return self.right.find(key)
        return None

if __name__ == '__main__':
    lst = [int(x) for x in input().split()]
    root = BinaryTree(lst[0])
    for x in lst[1:]:
        root.insert(x)
    current = root
    for x in lst[1:]:
        next_node = current.find(x)
        if next_node is None:
            print("NO")
            break
        if not (current.left == next_node or current.right == next_node):
            print("NO")
            break
        current = next_node
    else:
        print("YES")
