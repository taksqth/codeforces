import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    hor = defaultdict(int)
    ver = defaultdict(int)
    diag = defaultdict(int)
    rdiag = defaultdict(int)
    for _ in range(n):
        a, b = map(int, input().split())
        ver[a] += 1
        hor[b] += 1
        diag[a-b] += 1
        rdiag[a+b] += 1
    ans = 0
    for _, v in hor.items():
        ans += v * (v-1)
    for _, v in ver.items():
        ans += v * (v-1)
    for _, v in diag.items():
        ans += v * (v-1)
    for _, v in rdiag.items():
        ans += v * (v-1)
    sys.stdout.write(str(ans) + "\n")



t = int(input())
for _ in range(t):
    solve()
