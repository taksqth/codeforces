import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.maxdepth = [1] * n
        self.edges = [0] * n
        self.selfloop = [False] * n
        self.head = [True] * n

    def get_set(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.get_set(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        pi = self.get_set(i)
        pj = self.get_set(j)
        if i == j:
            self.selfloop[pi] = True
        if pi == pj:
            self.edges[pi] += 1
            return
        if self.maxdepth[pi] > self.maxdepth[pj]:
            pi, pj = pj, pi
        if self.maxdepth[pi] == self.maxdepth[pj]:
            self.maxdepth[pj] += 1
        self.parent[pi] = pj
        self.head[pi] = False
        self.selfloop[pj] = self.selfloop[pi] or self.selfloop[pj]
        self.size[pj] += self.size[pi]
        self.edges[pj] += 1 + self.edges[pi]


def solve():
    mod = 998244353
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    uf = UnionFind(n)
    for i in range(n):
        uf.union(a[i] - 1, b[i] - 1)

    ret = 1
    for s in range(n):
        if not uf.head[s]:
            continue
        if uf.edges[s] != uf.size[s]:
            return 0
        ret *= n if uf.selfloop[s] else 2
        ret %= mod
    return ret


t = int(input())
for _ in range(t):
    sys.stdout.write(str(solve()) + "\n")
