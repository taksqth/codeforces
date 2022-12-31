def solve():
    mod = 10**9 + 7
    n = int(input())

    son = (n * (n + 1) // 2) % mod
    sos = (n * (n + 1) * (2 * n + 1)) // 6 % mod
    ret = ((2 * sos - son) % mod) * 2022 % mod
    print(ret)


t = int(input())
for _ in range(t):
    solve()
