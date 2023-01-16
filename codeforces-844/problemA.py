def solve():
    w, d, h = map(int, input().split())
    a, b, f, g = map(int, input().split())
    ret = h
    md = float("inf")
    md = min(md, abs(a + f) + abs(b - g))
    md = min(md, abs(a - f) + abs(b + g))
    md = min(md, abs(a - f - 2 * (w - f)) + abs(b - g))
    md = min(md, abs(a - f) + abs(b - g - 2 * (d - g)))
    ret += md
    print(ret)


t = int(input())
for _ in range(t):
    solve()
