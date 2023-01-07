import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ret = 0
    for i in range(n):
        if a[i] % 2 == 1:
            ret += 1
    sys.stdout.write(str(ret) + "\n")


t = int(input())
for _ in range(t):
    solve()
