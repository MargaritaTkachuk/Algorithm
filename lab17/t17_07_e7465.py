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

def build_tree(arr):
    root = BinaryTree(arr[0])
    for x in arr[1:]:
        root.insert(x)
    return root

def is_same_tree(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return (
        t1.key == t2.key and
        is_same_tree(t1.left, t2.left) and
        is_same_tree(t1.right, t2.right)
    )


if __name__ == '__main__':
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))
    tree1 = build_tree(arr1)
    tree2 = build_tree(arr2)
    print(1 if is_same_tree(tree1, tree2) else 0)