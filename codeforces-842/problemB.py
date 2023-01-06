import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def solve():
    _, k = map(int, input().split())
    p = list(map(int, input().split()))

    d = deque()
    ret = 0
    for el in reversed(p):
        if len(d) > 0 and d[-1] < el:
            ret += 1
            while d[0] > el:
                d.popleft()
                ret += 1
        else:
            d.append(el)

    sys.stdout.write(str((ret + k - 1) // k) + "\n")


t = int(input())
for _ in range(t):
    solve()
