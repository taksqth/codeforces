import sys

mod = 10**9 + 7

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    ret = (pow(2, (n - 1), mod) * n) % mod
    tree = [set() for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u, v = u - 1, v - 1
        tree[u].add(v)
    while True:
        updated = False
        to_remove = set()
        for u in range(n):
            if len(tree[u]) == 0:
                to_remove.add(u)
            else:
                updated = True
                ret += pow(2, (n - 1), mod)
                ret %= mod
        if not updated:
            break
        for u in range(n):
            tree[u] = tree[u] - to_remove
    sys.stdout.write(str(ret) + "\n")


t = int(input())
for _ in range(t):
    solve()
