class IntervalTree:
    def __init__(self, a):
        self.t = [0] * (len(a) * 4 + 1)
        self.a = a
        self.length = len(a)
        self._build(1, 0, self.length - 1)

    def _build(self, v, tl, tr):
        if tl == tr:
            self.t[v] = self.a[tl]
        else:
            mid = (tl + tr) // 2
            self._build(v * 2, tl, mid)
            self._build(v * 2 + 1, mid + 1, tr)
            self.t[v] = self.t[v * 2] + self.t[v * 2 + 1]

    def query(self, l, r):
        def rquery(v, tl, tr, l, r):
            if l > r:
                return 0
            if l == tl and r == tr:
                return self.t[v]
            mid = (tl + tr) // 2
            return rquery(v * 2, tl, mid, l, min(r, mid)) + rquery(
                v * 2 + 1, mid + 1, tr, max(l, mid + 1), r
            )

        return rquery(1, 0, self.length - 1, l, r)

    def update(self, pos, new_val):
        self.a[pos] = new_val

        def rupdate(v, tr, tl, pos, new_val):
            if tl == tr:
                self.t[v] = new_val
            else:
                mid = (tl + tr) // 2
                if pos <= mid:
                    rupdate(v * 2, tl, mid, pos, new_val)
                else:
                    rupdate(v * 2 + 1, mid + 1, tr, pos, new_val)
                self.t[v] = self.t[v * 2] + self.t[v * 2 + 1]

        rupdate(1, 0, self.length - 1, pos, new_val)


t = IntervalTree([1, 2, 3, 4, 5, 6, 7])
print(t.query(0, 5))
t.update(0, 10)
print(t.query(0, 5))
