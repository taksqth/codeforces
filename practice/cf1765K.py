import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    m = []
    d = []
    s = 0
    for i in range(n):
        m.append(list(map(int, input().split())))
        d.append(m[i][n - i - 1])
        s += sum(m[i])

    sys.stdout.write(str(s - min(d)) + "\n")


solve()
