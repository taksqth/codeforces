import sys

input = lambda: sys.stdin.readline().rstrip()

n, a, b = map(int, input().split())
s = input()


def cost_palindrome(s, b):
    lo = 0
    hi = len(s) - 1
    ret = 0
    while lo <= hi:
        if s[lo] != s[hi]:
            ret += b
        lo += 1
        hi -= 1
    return ret


mincost = float("inf")
for i in range(n):
    mincost = min(mincost, i * a + cost_palindrome(s[i:] + s[:i], b))
sys.stdout.write(str(mincost) + "\n")
