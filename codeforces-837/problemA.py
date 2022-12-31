def solve():
    n = int(input())
    l = list(map(int, input().split()))
    maxn = max(l)
    minn = min(l)
    return (
        n * (n - 1)
        if all([el == minn for el in l])
        else l.count(maxn) * l.count(minn) * 2
    )


t = int(input())
for _ in range(t):
    print(solve())
