import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    ret = 0
    lrm = None
    for i in range(n - 1, -1, -1):
        if (lrm is None or i + 1 < lrm) and a[i] <= i:
            ret += 1
        lrm = a[i]
    if a[0] != 0:
        ret += 1
    print(ret)


t = int(input())
for _ in range(t):
    solve()
