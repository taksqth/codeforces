def solve():
    n = int(input())
    l = list(map(int, input().split()))

    inversions = 0
    zeroes = 0
    for i in range(n - 1, -1, -1):
        if l[i] == 0:
            zeroes += 1
        else:
            inversions += zeroes
    ones = 0
    maxgains = 0
    for i in range(n):
        if l[i] == 0:
            zeroes -= 1
            if maxgains < zeroes - ones:
                maxgains = zeroes - ones
        else:
            if maxgains < ones - zeroes:
                maxgains = ones - zeroes
            ones += 1

    print(inversions + maxgains)


t = int(input())
for _ in range(t):
    solve()
