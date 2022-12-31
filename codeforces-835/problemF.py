def solve():
    n, c, d = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    agg = 0
    for i in range(n):
        if i >= d:
            break
        agg += a[i]
        a[i] = agg
        if agg >= c:
            print("Infinity")
            return
    for i in range(d - 1, -1, -1):
        if (
            a[min(i, n - 1)] * (d // (i + 1))
            + (a[min((d % (i + 1)) - 1, n - 1)] if d % (i + 1) != 0 else 0)
            >= c
        ):
            print(str(i))
            return
    print("Impossible")


t = int(input())
for _ in range(t):
    solve()
