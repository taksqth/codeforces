def solve():
    n = int(input())
    l = list(map(int, input().split()))

    if n <= 2:
        print("YES")
        return

    up = False
    for i in range(1, n - 1):
        if l[i - 1] < l[i]:
            up = True
        if l[i + 1] < l[i] and up:
            print("NO")
            return
    print("YES")


t = int(input())
for _ in range(t):
    solve()
