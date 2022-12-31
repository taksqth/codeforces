def solve():
    l = list(map(int, input().split()))
    l.sort()
    print(l[1])

t = int(input())
for _ in range(t):
    solve()