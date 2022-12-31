def solve():
    n, m = tuple(map(int, input().split()))
    closest = [n] * n
    for _ in range(m):
        f1, f2 = tuple(map(int, input().split()))
        f1, f2 = sorted((f1 - 1, f2 - 1))
        closest[f1] = min(closest[f1], f2)
    cnt = [n - 1] * n
    for i in range(n - 2, -1, -1):
        cnt[i] = min(cnt[i + 1], closest[i] - 1)
    for i in range(n - 1, -1, -1):
        cnt[i] = cnt[i] - i + 1
    print(sum(cnt))


t = int(input())
for _ in range(t):
    solve()
