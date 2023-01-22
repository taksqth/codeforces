class IntervalTree:
    def __init__(self, l):
        self.l = l
        self.size = len(l)
        self.t = [0] * (self.size * 4 + 1)
        self.build()

    def build(self):
        def buildr(v, tl, tr):
            if tl == tr:
                self.t[v] = self.l[tl]
                return
            mid = (tl + tr) // 2
            buildr(v * 2, tl, mid)
            buildr(v * 2 + 1, mid + 1, tr)
            self.t[v] = self.t[v * 2] + self.t[v * 2 + 1]

        buildr(1, 0, self.size - 1)

    def update(self, pos, val):
        self.l[pos] = val

        def updater(v, tl, tr, pos, val):
            if tl == tr:
                self.t[v] = val
                return
            mid = (tl + tr) // 2
            if pos <= mid:
                updater(v * 2, tl, mid, pos, val)
            else:
                updater(v * 2 + 1, mid + 1, tr, pos, val)
            self.t[v] = self.t[v * 2] + self.t[v * 2 + 1]

        updater(1, 0, self.size - 1, pos, val)

    def query(self, l, r):
        def queryr(v, tl, tr, l, r):
            if l > r:
                return 0
            if tl == l and tr == r:
                return self.t[v]
            mid = (tl + tr) // 2
            return queryr(v * 2, tl, mid, l, min(mid, r)) + queryr(
                v * 2 + 1, mid + 1, tr, max(l, mid + 1), r
            )

        return queryr(1, 0, self.size - 1, l, r)


t = IntervalTree([1, 2, 3, 4, 5, 6, 7])
print(t.query(0, 5))
t.update(0, 10)
print(t.query(0, 5))
