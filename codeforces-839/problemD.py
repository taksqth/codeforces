import math


def solve():
    upper_bound = 10**8 + 1
    lower_bound = 0
    n = int(input())
    l = list(map(int, input().split()))
    for i in range(n):
        if i > 0 and l[i] < l[i - 1]:
            bound = math.ceil((l[i] + l[i - 1]) / 2)
            if bound > lower_bound:
                lower_bound = bound
        if i < n - 1 and l[i] < l[i + 1]:
            bound = math.floor((l[i] + l[i + 1]) / 2)
            if bound < upper_bound:
                upper_bound = bound
    if lower_bound <= upper_bound:
        print(lower_bound)
    else:
        print(-1)


t = int(input())
for _ in range(t):
    solve()
