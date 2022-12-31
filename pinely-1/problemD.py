n, k = tuple(map(int, input().split()))
dp = [[[0, 0] for _ in range(k + 2)] for _ in range(n)]
dp[0][0][0] = 3
dp[0][1][1] = 1
for i in range(1, n):
    for j in range(k + 1):
        dp[i][j][0] += dp[i - 1][j][0] + dp[i - 1][j][1]
        dp[i][j][0] += 2 * dp[i - 1][j][0]
        if j > 0:
            dp[i][j][1] += 2 * dp[i - 1][j - 1][1]
            dp[i][j][1] += dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1]
print((dp[n - 1][k][0] + dp[n - 1][k][1]))
