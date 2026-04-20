import sys
sys.setrecursionlimit(10**7)

class Node:
    def __init__(self, key = None, color = 0):
        self.mKey = key
        self.mColor = color

    def empty(self):
        return self.mKey is None

    def setKey(self, key):
        self.mKey = key

    def key(self):
        return self.mKey

    def setColor(self, color):
        self.mColor = color

    def color(self):
        return self.mColor

class Tree(Node):
    def __init__(self, key = None, color = 0):
        super().__init__(key, color)
        self.mChildren = []

    def empty(self):
        return super().empty() and len(self.mChildren) == 0

    def addChild(self, child):
        self.mChildren.append(child)

    def removeChild(self, key):
        for child in self.mChildren:
            if child.key() == key:
                self.mChildren.remove(child)
                return True
        return False

    def getChild(self, key):
        for child in self.mChildren:
            if child.key() == key:
                return child
        return None

    def getChildren(self):
        return self.mChildren

def dfs(node, answer):
    colors = set()
    colors.add(node.color())

    for child in node.getChildren():
        child_colors = dfs(child, answer)

        if len(child_colors) > len(colors):
            colors, child_colors = child_colors, colors

        colors |= child_colors

    answer[node.key()] = len(colors)
    return colors

if __name__ == '__main__':
    n = int(input())

    nodes = [None] * (n + 1)
    parent = [0] * (n + 1)

    for i in range(1, n + 1):
        p, c = map(int, input().split())
        nodes[i] = Tree(i, c)
        parent[i] = p

    root = None

    for i in range(1, n + 1):
        if parent[i] == 0:
            root = nodes[i]
        else:
            nodes[parent[i]].addChild(nodes[i])

    answer = [0] * (n + 1)

    dfs(root, answer)

    for i in range(1, n + 1):
        print(answer[i], end=' ')





