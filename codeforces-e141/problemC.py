import sys
import bisect

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    vic = [i for i in range(n)]

    a = [(el, i) for i, el in enumerate(a)]
    a.sort()
    i = 0
    myvic = 0
    while i < n and m >= a[i][0]:
        m -= a[i][0]
        i += 1
        myvic += 1
    for el, j in a:
        if myvic > 0 and vic[j] == myvic and m >= el - a[i - 1][0]:
            vic[a[i - 1][1]] += 1
            vic[j] -= 1
    for j in range(i, n):
        vic[a[j][1]] += 1
    vic.sort()
    i = n - bisect.bisect_right(vic, myvic) + 1
    sys.stdout.write(str(i) + "\n")


t = int(input())
for _ in range(t):
    solve()
