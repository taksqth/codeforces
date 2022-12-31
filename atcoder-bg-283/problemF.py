n = int(input())
p = list(map(int, input().split()))

d = [float("inf")] * n
for i in range(n):
    t = p[i]
    offset = 1
    while d[i] > offset:
        cand = [d[i]]
        if i - offset >= 0:
            cand.append(abs(p[i] - p[i - offset]) + offset)
        if i + offset < n:
            cand.append(abs(p[i] - p[i + offset]) + offset)
        d[i] = min(cand)
        offset += 1

print(" ".join(map(str, d)))
