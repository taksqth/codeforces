class FenwickTree:
    def __init__(self, l):
        self.l = [0] * len(l)
        self.tree = [0] * (len(l) + 1)
        for i, el in enumerate(l):
            self.update(i, el)

    def update(self, i, v):
        diff = v - self.l[i]
        self.l[i] = v
        i = i + 1
        while i < len(self.tree):
            self.tree[i] += diff
            i += i & -i

    def query(self, i):
        i = i + 1
        ret = 0
        while i != 0:
            ret += self.tree[i]
            i ^= i & -i
        return ret


t = FenwickTree([1, 2, 3, 4, 5, 6, 7])
print(t.query(5))
t.update(0, 10)
print(t.query(5))
