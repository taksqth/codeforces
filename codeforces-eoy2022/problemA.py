import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(m):
        minj = 0
        for j in range(1, n):
            if a[j] < a[minj]:
                minj = j
        a[minj] = b[i]
    sys.stdout.write(str(sum(a)) + "\n")


t = int(input())
for _ in range(t):
    solve()
