import io, os, sys

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def solve():
    n = int(input().decode())
    s = input().decode()[:-1]
    dp = [[0] * n for _ in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            if i + j > n:
                continue
            if s[i - 1] == s[n - j]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    ret = 0
    for i in range(n - 1):
        if dp[n - i - 1][i + 1] > ret:
            ret = dp[n - i - 1][i + 1]
    sys.stdout.write(str(ret) + "\n")


t = int(input().decode())
for _ in range(t):
    solve()
