import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    k = int(input())
    sys.stdout.write(str(k - 1) + "\n")


t = int(input())
for _ in range(t):
    solve()
