def solve():
    _ = int(input())
    l = list(map(int, input().split()))
    top = 0
    topi = -1
    top2 = 0
    for i, el in enumerate(l):
        if el >= top:
            top2 = top
            top = el
            topi = i
        elif el > top2:
            top2 = el
    ret = []
    for i, el in enumerate(l):
        if i != topi:
            ret.append(el - top)
        else:
            ret.append(el - top2)
    print(" ".join(map(str, ret)))


t = int(input())
for _ in range(t):
    solve()
