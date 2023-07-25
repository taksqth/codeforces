import sys
import math

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n, c = map(int, input().split())
    s = list(map(int, input().split()))
    cnt = 0
    cntsq = 0
    for i in range(n):
        cnt += s[i]
        cntsq += s[i]*s[i]
    c -= cntsq
    x = (-cnt + math.sqrt(cnt*cnt + n*c)) / (2*n)
    sys.stdout.write(str(int(x)) + "\n")



t = int(input())
for _ in range(t):
    solve()
