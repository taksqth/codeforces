import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


class DSU:
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


def solve():
    n = int(input())
    p = list(map(int, input().split()))

    dsu = DSU(n + 1)

    for el in p:
        while not dsu.same_set(el, p[el - 1]):
            dsu.union(el, p[el - 1])
            el = p[el - 1]
    noswap = -1
    for i in range(1, n + 1):
        if dsu.same_set(i, i - 1):
            noswap = dsu.parent[i]
            break
    ret = 0
    for i in range(n + 1):
        if i == dsu.parent[i]:
            ret += dsu.set_sizes[i] - 1
            if i == noswap:
                ret -= 1
    if noswap == -1:
        ret += 1
    sys.stdout.write(str(ret) + "\n")


t = int(input())
for _ in range(t):
    solve()
