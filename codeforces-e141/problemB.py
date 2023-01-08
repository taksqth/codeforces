import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n = int(input())

    numbers = [
        (-1) ** i * (i + 1) // 2 + (n**2 if i % 2 == 1 else 0) + 1
        for i in range(n**2)
    ]

    m = [[0] * n for _ in range(n)]
    for ind in range(n**2):
        i = ind // n
        j = (-1) ** i * (ind % n) + (n - 1 if i % 2 == 1 else 0)
        m[i][j] = numbers[ind]

    for row in m:
        sys.stdout.write(" ".join(map(str, row)) + "\n")


t = int(input())
for _ in range(t):
    solve()
