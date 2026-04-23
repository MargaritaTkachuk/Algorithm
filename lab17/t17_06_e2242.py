class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = BinaryTree(key)
            else:
                self.left.insert(key)
        elif key >= self.key:
            if self.right is None:
                self.right = BinaryTree(key)
            else:
                self.right.insert(key)

    def preorder(self):
        result = self.key
        if self.left:
            result += self.left.preorder()
        if self.right:
            result += self.right.preorder()
        return result


if __name__ == '__main__':
    lines = []
    while True:
        line = input().strip()
        if line == '*':
            break
        if line:
            lines.append(line)
    if not lines:
        print()
    else:
        root = None
        for line in reversed(lines):
            for ch in line:
                if root is None:
                    root = BinaryTree(ch)
                else:
                    root.insert(ch)
        print(root.preorder())