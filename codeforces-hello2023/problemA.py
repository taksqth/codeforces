import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    _ = int(input())
    s = input()

    if "L" not in s or "R" not in s:
        sys.stdout.write("-1\n")
        return

    lo = 0
    while lo < len(s) and s[lo] == "L":
        lo += 1

    hi = len(s) - 1
    while hi >= 0 and s[hi] == "R":
        hi -= 1

    if lo > hi:
        sys.stdout.write(str(lo) + "\n")
        return
    sys.stdout.write("0\n")


t = int(input())
for _ in range(t):
    solve()
