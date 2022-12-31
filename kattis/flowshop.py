n, m = tuple(map(int, input().split()))
p = []
p.append([0] * (m + 1))
for i in range(n):
    p.append([0] + list(map(int, input().split())))

ret = []
for j in range(1, m + 1):
    for i in range(1, n + 1):
        p[i][j] += max(p[i][j - 1], p[i - 1][j])
        if j == m:
            ret.append(p[i][j])

print(" ".join(map(str, ret)))
