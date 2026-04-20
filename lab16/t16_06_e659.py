
class Node:
    def __init__(self, key=None, val=0):
        self.mKey = key
        self.mVal = val

    def empty(self):
        return self.mKey is None

    def setKey(self, key):
        self.mKey = key

    def key(self):
        return self.mKey

    def setValue(self, val):
        self.mVal = val

    def value(self):
        return self.mVal


class Tree(Node):
    def __init__(self, key=None, val=0):
        super().__init__(key, val)
        self.mChildren = []

    def empty(self):
        return super().empty() and len(self.mChildren) == 0

    def addChild(self, child):
        self.mChildren.append(child)

    def getChildren(self):
        return self.mChildren

def dfs(node, is_max_player):
    if len(node.getChildren()) == 0:
        return node.value()

    if is_max_player:
        best = -10**9
        for child in node.getChildren():
            best = max(best, dfs(child, False))
        return best
    else:
        best = 10**9
        for child in node.getChildren():
            best = min(best, dfs(child, True))
        return best

if __name__ == '__main__':
    n = int(input())

    nodes = [None] * (n + 1)
    for i in range(1, n + 1):
        nodes[i] = Tree(i)

    for i in range(2, n + 1):
        data = input().split()

        if data[0] == 'L':
            parent = int(data[1])
            val = int(data[2])
            nodes[i].setValue(val)
            nodes[parent].addChild(nodes[i])
        else:
            parent = int(data[1])
            nodes[parent].addChild(nodes[i])

    result = dfs(nodes[1], True)

    if result == 1:
        print("+1")
    elif result == -1:
        print("-1")
    else:
        print("0")