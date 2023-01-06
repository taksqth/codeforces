import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a = [[el, i] for i, el in enumerate(a)]
    a.sort(reverse=True)

    cnt = [[True, True] for i in range(n + 1)]
    p = [0] * n
    q = [0] * n

    for el, i in a:
        if cnt[el][0]:
            cnt[el][0] = False
            p[i] = el
        elif cnt[el][1]:
            cnt[el][1] = False
            q[i] = el
        else:
            sys.stdout.write("NO\n")
            return
    pn = n
    qn = n
    for el, i in a:
        if p[i] == 0:
            while pn > q[i] or not cnt[pn][0]:
                pn -= 1
                if pn == 0:
                    sys.stdout.write("NO\n")
                    return
            cnt[pn][0] = False
            p[i] = pn
        if q[i] == 0:
            while qn > p[i] or not cnt[qn][1]:
                qn -= 1
                if qn == 0:
                    sys.stdout.write("NO\n")
                    return
            cnt[qn][1] = False
            q[i] = qn
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, p)) + "\n")
    sys.stdout.write(" ".join(map(str, q)) + "\n")


t = int(input())
for _ in range(t):
    solve()
