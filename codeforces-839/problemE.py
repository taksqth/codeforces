def solve():
    n = int(input())
    l = list(map(int, input().split()))
    oop_asc = set([i for i, el in enumerate(l) if el != i + 1])
    oop_desc = set([i for i, el in enumerate(l) if el != n - i])
    inter = oop_asc.intersection(oop_desc)
    oop_asc = oop_asc.difference(inter)
    oop_desc = oop_desc.difference(inter)

    if len(oop_asc) + len(inter) <= len(oop_desc):
        print("First")
    elif len(oop_asc) > len(oop_desc) + len(inter):
        print("Second")
    else:
        print("Tie")


t = int(input())
for _ in range(t):
    solve()
