# cook your dish here
def solve():
    _ = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = [min(ea, eb) for ea, eb in zip(a, b)]
    print(m)
    mstreak = 0
    streak = 0
    for el in m:
        if el > 0:
            streak += 1
        else:
            streak = 0
        if streak > mstreak:
            mstreak = streak
    print(mstreak)


t = int(input())
for _ in range(t):
    solve()
