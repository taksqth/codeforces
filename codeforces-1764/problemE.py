def solve():
    n, k = tuple(map(int, input().split()))
    a = []
    b = []
    line = {}
    for _ in range(n):
        ai, bi = tuple(map(int, input().split()))
        a.append(ai)
        b.append(bi)
    if k > a[0] + b[0]:
        print("NO")
    range(k - b[0], a[0])


t = int(input())
for _ in range(t):
    solve()
