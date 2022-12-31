h, w = map(int, input().split())
m = [[2] * (w + 2)]
for _ in range(h):
    m.append([2] + list(map(int, input().split())) + [2])
m.append([2] * (w + 2))


def flip(r):
    return list(map(lambda el: 1 - el, r))


def check_valid(rp, rr, rn):
    return all(
        [
            rr[j] == rr[j - 1] or rr[j] == rr[j + 1] or rr[j] == rp[j] or rr[j] == rn[j]
            for j in range(1, w + 1)
        ]
    )


dp = [[float("inf")] * 4 for _ in range(h + 1)]
dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0
dp[0][3] = 0
for i in range(h):
    if check_valid(m[i], m[i + 1], m[i + 2]):
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0])

    if check_valid(flip(m[i]), m[i + 1], m[i + 2]):
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][1])

    if check_valid(m[i], flip(m[i + 1]), m[i + 2]):
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][2] + 1)

    if check_valid(flip(m[i]), flip(m[i + 1]), m[i + 2]):
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][3] + 1)

    if check_valid(m[i], m[i + 1], flip(m[i + 2])):
        dp[i + 1][2] = min(dp[i + 1][2], dp[i][0])

    if check_valid(flip(m[i]), m[i + 1], flip(m[i + 2])):
        dp[i + 1][2] = min(dp[i + 1][2], dp[i][1])

    if check_valid(m[i], flip(m[i + 1]), flip(m[i + 2])):
        dp[i + 1][3] = min(dp[i + 1][3], dp[i][2] + 1)

    if check_valid(flip(m[i]), flip(m[i + 1]), flip(m[i + 2])):
        dp[i + 1][3] = min(dp[i + 1][3], dp[i][3] + 1)
sol = min(dp[h])
sol = sol if sol != float("inf") else -1
print(sol)
