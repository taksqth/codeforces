def solve():
    n, m = map(int, input().split())

    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    lo = 2
    hi = min(n, m)

    def valid(mid):
        valid = [[1 if a[i][j] >= mid else 0 for j in range(m)] for i in range(n)]
        for i in range(1, n):
            for j in range(m):
                valid[i][j] += valid[i - 1][j]
        for j in range(1, m):
            for i in range(n):
                valid[i][j] += valid[i][j - 1]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i >= mid:
                    valid[i][j] -= valid[i - mid][j]
                if j >= mid:
                    valid[i][j] -= valid[i][j - mid]
                if i >= mid and j >= mid:
                    valid[i][j] += valid[i - mid][j - mid]
                if valid[i][j] >= mid * mid:
                    return True
        return False

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if valid(mid):
            lo = mid + 1
        else:
            hi = mid - 1
    print(lo - 1)


t = int(input())
for _ in range(t):
    solve()
