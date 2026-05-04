from math import log2, ceil, inf


class SegmentTreeMin:
    def __init__(self, array):
        k = len(array)
        p = ceil(log2(k))
        n = 1 << p
        self.tree = [inf] * (2 * n)
        for i in range(k):
            self.tree[i + n] = array[i]
        for i in range(n - 1, 0, -1):
            self.tree[i] = min(self.tree[2*i], self.tree[2*i + 1])
        self.n = n

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = min(self.tree[2*i], self.tree[2*i + 1])

    def get_min(self, left, right):
        left += self.n
        right += self.n
        res = inf
        while left <= right:
            if left % 2 == 1:
                res = min(res, self.tree[left])
            if right % 2 == 0:
                res = min(res, self.tree[right])
            left = (left + 1) // 2
            right = (right - 1) // 2
        return res


class SegmentTreeMax:
    def __init__(self, array):
        k = len(array)
        p = ceil(log2(k))
        n = 1 << p
        self.tree = [-inf] * (2 * n)
        for i in range(k):
            self.tree[i + n] = array[i]
        for i in range(n - 1, 0, -1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i + 1])
        self.n = n

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = max(self.tree[2*i], self.tree[2*i + 1])

    def get_max(self, left, right):
        left += self.n
        right += self.n
        res = -inf
        while left <= right:
            if left % 2 == 1:
                res = max(res, self.tree[left])
            if right % 2 == 0:
                res = max(res, self.tree[right])
            left = (left + 1) // 2
            right = (right - 1) // 2
        return res


if __name__ == '__main__':
    f = open("input.txt")
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))
    m = int(f.readline())
    tree_min = SegmentTreeMin(arr)
    tree_max = SegmentTreeMax(arr)
    for _ in range(m):
        q, l, r = map(int, f.readline().split())
        if q == 1:
            mn = tree_min.get_min(l - 1, r - 1)
            mx = tree_max.get_max(l - 1, r - 1)
            if mn == mx:
                print("draw")
            else:
                print("wins")
        else:
            tree_min.update(l - 1, r)
            tree_max.update(l - 1, r)
    f.close()