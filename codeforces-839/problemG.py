def solve():
    n, x, y = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    gains = [2*(len(l)-i) for i in range(len(l))]
    gi = 0
    while x > l[gi]:
        gi += 1
    while x < y - gains[gi]:

    for el in range(el):

t = int(input())
for _ in range(t):
    solve()
