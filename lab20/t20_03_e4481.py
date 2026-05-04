from math import log2, ceil, gcd


class SegmentTree:

    def __init__(self, array):
        k = len(array)
        p = ceil(log2(k))
        n = 1 << p
        self.tree = [0] * 2 * n
        for i in range(k):
            self.tree[i + n] = array[i]
        for i in range(n - 1, 0, -1):
            self.tree[i] = gcd(self.tree[2*i], self.tree[2*i + 1])
        self.n = n

    def update(self, i, item):
        i = self.n + i
        self.tree[i] = item
        while i > 1:
            i //= 2
            self.tree[i] = gcd(self.tree[2*i], self.tree[2*i + 1])

    def gcd_(self, left, right):
        left += self.n
        right += self.n
        result = 0
        while left <= right:
            if left % 2 == 1:
                result = gcd(result, self.tree[left])
            if right % 2 == 0:
                result = gcd(result, self.tree[right])
            left = (left + 1) // 2
            right = (right - 1) // 2
        return result


if __name__ == '__main__':
    f = open("input.txt")
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))
    m = int(f.readline())
    tree = SegmentTree(arr)
    for _ in range(m):
        q, l, r = map(int, f.readline().split())
        if q == 1:
            print(tree.gcd_(l - 1, r - 1))
        elif q == 2:
            tree.update(l - 1, r)
    f.close()