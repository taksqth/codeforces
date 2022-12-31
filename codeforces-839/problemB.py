def solve():
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    for _ in range(4):
        if a < b and a < c and b < d and c < d:
            print("YES")
            return
        a, b, d, c = b, d, c, a
    print("NO")


t = int(input())
for _ in range(t):
    solve()
