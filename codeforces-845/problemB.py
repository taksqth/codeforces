import sys

input = lambda: sys.stdin.readline().rstrip()

mod = 10**9 + 7
limit = 10**5 + 1
fact = [1] * limit
for i in range(2, limit):
    fact[i] = (i * fact[i - 1]) % mod


def solve():
    n = int(input())
    ret = ((n - 1) * n * fact[n]) % mod
    sys.stdout.write(str(ret) + "\n")


t = int(input())
for _ in range(t):
    solve()
