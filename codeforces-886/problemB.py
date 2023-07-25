import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    mv, mi = 0, 0
    for i in range(n):
        a, b = map(int, input().split())
        if a <= 10 and b > mv:
            mv = b
            mi = i
    sys.stdout.write(str(mi + 1) + "\n")


t = int(input())
for _ in range(t):
    solve()
