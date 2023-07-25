import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    mc = 1
    c = 1
    for i in range(n-1):
        if a[i+1] - a[i] <= k:
            c += 1
        else:
            c = 1
        if c > mc:
            mc = c
    sys.stdout.write(str(n-mc) + "\n")


t = int(input())
for _ in range(t):
    solve()
