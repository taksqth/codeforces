import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    valid = set(range(3))
    hs = [h, h, h]
    hc = [0, 0, 0]
    p = [[3, 2, 2], [2, 3, 2], [2, 2, 3]]
    for el in a:
        nvalid = valid.copy()
        for i in valid:
            while el >= hs[i] and len(p[i]) > 0:
                hs[i] *= p[i].pop()
            if el < hs[i]:
                hc[i] += 1
                hs[i] += el // 2
            else:
                nvalid.remove(i)
        valid = nvalid
        if len(valid) == 0:
            break

    sys.stdout.write(str(max(hc)) + "\n")


t = int(input())
for _ in range(t):
    solve()
