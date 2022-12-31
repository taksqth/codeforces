from functools import reduce


def solve():
    _ = int(input())
    a = list(map(int, input().split()))
    r = reduce(lambda x, y: x * y, a)
    r += len(a) - 1
    print(r * 2022)


t = int(input())
for _ in range(t):
    solve()
