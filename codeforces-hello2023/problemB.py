import sys
import math

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    if n == 2:
        sys.stdout.write("YES\n1 1\n")
        return

    a = math.ceil(n / 2) - 1
    b = n // 2 - 1
    if b == 0:
        sys.stdout.write("NO\n")
        return

    r = []
    for i in range(n):
        r.append(b if i % 2 == 0 else -a)
    sys.stdout.write("YES\n" + " ".join(map(str, r)) + "\n")


t = int(input())
for _ in range(t):
    solve()
