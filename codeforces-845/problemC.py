import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))


t = int(input())
for _ in range(t):
    solve()
