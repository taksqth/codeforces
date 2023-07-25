import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = Counter(a)
    l = [0] * (n+1)
    for k, v in cnt.items():
        for i in range(k, n+1, k):
            l[i] += v
    sys.stdout.write(str(max(l)) + "\n")




t = int(input())
for _ in range(t):
    solve()
