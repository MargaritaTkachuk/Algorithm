
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


def dfs(node):

    if len(node.getChildren()) == 0:
        return node.value()

    min_cost = float('inf')

    for child in node.getChildren():
        min_cost = min(min_cost, dfs(child))

    return node.value() + min_cost


if __name__ == '__main__':
    n = int(input())

    nodes = [None] * (n + 1)

    for i in range(1, n + 1):
        nodes[i] = Tree(i)

    for i in range(1, n + 1):
        data = list(map(int, input().split()))
        cost = data[0]
        k = data[1]
        children = data[2:]

        nodes[i].setValue(cost)

        for child_id in children:
            nodes[i].addChild(nodes[child_id])

    result = dfs(nodes[1])

    print(result)