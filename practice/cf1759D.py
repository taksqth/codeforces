import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n, m = map(int, input().split())

    cnt = Counter()
    ne = n
    for el in [2, 5]:
        while ne % el == 0:
            cnt[el] += 1
            ne //= el

    k = 1
    while cnt[5] < cnt[2] and k * 5 <= m:
        k *= 5
        cnt[5] += 1
    while cnt[2] < cnt[5] and k * 2 <= m:
        k *= 2
        cnt[2] += 1
    while k * 10 <= m:
        k *= 10
    if k * n == n:
        sys.stdout.write(str(n * m) + "\n")
        return
    sys.stdout.write(str(n * k * (m // k)) + "\n")


t = int(input())
for _ in range(t):
    solve()
