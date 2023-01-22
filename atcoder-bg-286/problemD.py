import sys

input = lambda: sys.stdin.readline().rstrip()

n, x = map(int, input().split())
coins = []
for _ in range(n):
    a, b = map(int, input().split())
    for _ in range(b):
        coins.append(a)


dp = [[0] * (x + 1) for _ in range(len(coins) + 1)]
for j in range(1, x + 1):
    dp[0][j] = float("inf")

for i, coin in enumerate(coins, 1):
    for j in range(1, x + 1):
        if coin == j:
            dp[i][j] = 1
        elif coin > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = min(dp[i - 1][j], 1 + dp[i - 1][j - coin])
if dp[-1][-1] < float("inf"):
    sys.stdout.write("Yes\n")
else:
    sys.stdout.write("No\n")
