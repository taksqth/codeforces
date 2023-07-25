import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    a, b, c = map(int, input().split())
    if a + b > 9 or a + c > 9 or b + c > 9:
        sys.stdout.write("Yes\n")
    else:
        sys.stdout.write("No\n")


t = int(input())
for _ in range(t):
    solve()
