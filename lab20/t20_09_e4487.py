class SegmentTree:
    def __init__(self, a):
        self.n = len(a)
        self.t = [(0, 0, 0, 0, 0, 0)] * (4 * self.n)
        self.build(a, 1, 0, self.n - 1)

    def make(self, x):
        return (x, x, 1, 1, 1, 1)

    def merge(self, L, R):
        if L[5] == 0:
            return R
        if R[5] == 0:
            return L

        first = L[0]
        last = R[1]
        length = L[5] + R[5]

        pref = L[2]
        if L[2] == L[5] and L[1] <= R[0]:
            pref = L[5] + R[2]

        suf = R[3]
        if R[3] == R[5] and L[1] <= R[0]:
            suf = R[5] + L[3]

        best = max(L[4], R[4])
        if L[1] <= R[0]:
            best = max(best, L[3] + R[2])

        return (first, last, pref, suf, best, length)

    def build(self, a, v, tl, tr):
        if tl == tr:
            self.t[v] = self.make(a[tl])
        else:
            tm = (tl + tr) // 2
            self.build(a, v*2, tl, tm)
            self.build(a, v*2+1, tm+1, tr)
            self.t[v] = self.merge(self.t[v*2], self.t[v*2+1])

    def update(self, v, tl, tr, pos, val):
        if tl == tr:
            self.t[v] = self.make(val)
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(v*2, tl, tm, pos, val)
            else:
                self.update(v*2+1, tm+1, tr, pos, val)
            self.t[v] = self.merge(self.t[v*2], self.t[v*2+1])

    def query(self, v, tl, tr, l, r):
        if l > r:
            return (0, 0, 0, 0, 0, 0)
        if l == tl and r == tr:
            return self.t[v]
        tm = (tl + tr) // 2
        left = self.query(v*2, tl, tm, l, min(r, tm))
        right = self.query(v*2+1, tm+1, tr, max(l, tm+1), r)
        return self.merge(left, right)


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        a = list(map(int, f.readline().split()))
        m = int(f.readline())

        st = SegmentTree(a)

        for _ in range(m):
            t, l, r = map(int, f.readline().split())
            if t == 1:
                res = st.query(1, 0, n-1, l-1, r-1)
                print(res[4])
            else:
                st.update(1, 0, n-1, l-1, r)