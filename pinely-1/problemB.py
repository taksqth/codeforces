def solve_case():
    n = int(input())
    l = list(map(int, input().split()))
    d = set()
    for el in l:
        d.add(el)
    if len(d) == 2:
        print(2 + (len(l) - 2) // 2)
    else:
        print(len(l))


t = int(input())
for _ in range(t):
    solve_case()
