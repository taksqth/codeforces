def solve():
    _ = int(input())
    s = input()
    mod = 998244353

    dp = [0] * (27 * 27)
    dp[0] = 1
    for l in s:
        dpn = [0] * (27 * 27)
        if l != "?":
            l = ord(l) - ord("a") + 1
            for l2 in range(27):
                if l2 != l:
                    dpn[l * 27 + l2] += sum(
                        [dp[l2 * 27 + l3] for l3 in range(27) if l3 != l]
                    )
                    dpn[l * 27 + l2] %= mod
        else:
            for l in range(1, 27):
                for l2 in range(27):
                    if l2 != l:
                        dpn[l * 27 + l2] += sum(
                            [dp[l2 * 27 + l3] for l3 in range(27) if l3 != l]
                        )
        dp = dpn
    return sum(dpn) % mod


print(solve())
