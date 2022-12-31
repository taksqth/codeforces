def solve():
    n, _, k = map(int, (input().split()))
    l = list(map(int, (input().split())))
    maj = 0
    cntmaj = 1
    for el in l:
        if el == maj:
            cntmaj += 1
        if maj < el:
            maj = el
            cntmaj = 1
    extra_slots = n - (maj - 1) * k
    if cntmaj <= extra_slots:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    solve()
