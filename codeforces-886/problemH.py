import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()


def solve():
    _, m = map(int, input().split())
    pos = defaultdict(int)
    possible = True
    for _ in range(m):
        a, b, d = map(int, input().split())
        if not possible:
            continue
        if a not in pos and b not in pos:
            pos[a] = 0
            pos[b] = d
        elif a not in pos and b in pos:
            pos[a] = pos[b] - d
        elif a in pos and b not in pos:
            pos[b] = pos[a] + d
        else:
            if pos[a] + d != pos[b]:
                possible = False
    if possible:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")



t = int(input())
for _ in range(t):
    solve()
