import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    s = list(map(int, input()))

    mod = 998244353

    ret = 0
    ones = 0
    zeroes = 0
    for i in range(n):
        ones += s[i]
        zeroes += 1 - s[i]
        if s[i] == 1:
            inc = pow(2, (max(0, min(i, ones - zeroes - 1))), mod)
            ones += max(0, zeroes - ones + 1)
        else:
            inc = pow(2, (max(0, min(i, zeroes - ones - 1))), mod)
            zeroes += max(0, ones - zeroes + 1)
        ret += inc
        ret %= mod

    sys.stdout.write(str(ret) + "\n")


t = int(input())
for _ in range(t):
    solve()
