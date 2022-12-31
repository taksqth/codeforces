class UnionFind:
    def __init__(self, size):
        self.nsets = size
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
        self.set_sizes = [1] * size

    def find_set(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find_set(self.parent[i])
        return self.parent[i]

    def same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)

    def size_of_set(self, i):
        return self.set_sizes[self.find_set(i)]

    def union(self, i, j):
        x = self.find_set(i)
        y = self.find_set(j)
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        self.parent[x] = y
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        self.set_sizes[y] += self.set_sizes[x]
        self.nsets -= 1


uf = UnionFind(5)
print(uf.nsets)
uf.union(0, 1)
print(uf.nsets)
uf.union(2, 3)
print(uf.nsets)
uf.union(4, 3)
print(uf.nsets)
print(f" isSameSet(0, 3) = {uf.same_set(0, 3)}")  # 0 (false)
print(f" isSameSet(4, 3) = {uf.same_set(4, 3)}")  # 1 (true)
for i in range(5):
    print(f" findSet(%d) = {uf.find_set(i)}, sizeOfSet(%d) = {uf.size_of_set(i)}")
uf.union(0, 3)
print(uf.nsets)
for i in range(5):
    print(f" findSet(%d) = {uf.find_set(i)}, sizeOfSet(%d) = {uf.size_of_set(i)}")
