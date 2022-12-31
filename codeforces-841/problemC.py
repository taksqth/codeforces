def solve():
    n = int(input())
    a = list(map(int, input().split()))
    m = [0] * (2 * n)

    cur = 0
    m[0] += 1
    cnt = 0
    for j in range(n):
        cur ^= a[j]
        for i in range(n):
            if i * i > 2 * n:
                break
            if cur ^ i * i < 2 * n:
                cnt += m[cur ^ i * i]
        m[cur] += 1
    print(n * (n + 1) // 2 - cnt)


t = int(input())
for _ in range(t):
    solve()
