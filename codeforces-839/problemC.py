def solve():
    k, n = map(int, input().split())
    ret = []
    i = 1
    j = 1
    while i <= n:
        ret.append(i)
        if len(ret) == k or k - len(ret) > n - (i + j - 1):
            break
        i += j
        j += 1
    while len(ret) < k:
        i += 1
        ret.append(i)
    print(" ".join(map(str, ret)))


t = int(input())
for _ in range(t):
    solve()
