import math
from functools import reduce


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    i = reduce(math.gcd, a)
    m = max(a)
    print(m // i)


t = int(input())
for _ in range(t):
    solve()
