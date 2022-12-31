def solve():
    n, m = map(int, input().split())
    table = []
    rcnt = [0] * n
    totone = 0
    for i in range(n):
        table.append(list(map(int, input().split())))
        rcnt[i] = sum(table[-1])
        totone += rcnt[i]
    if totone % n != 0:
        print(-1)
        return
    target = totone // n
    swaps = sum([max(el - target, 0) for el in rcnt])
    print(swaps)
    for j in range(m):
        zqueue = []
        oqueue = []
        for i in range(n):
            if rcnt[i] > target and table[i][j] == 1:
                if len(zqueue) > 0:
                    si = zqueue.pop()
                    rcnt[i] -= 1
                    rcnt[si] += 1
                    print(i + 1, si + 1, j + 1)
                else:
                    oqueue.append(i)
            elif rcnt[i] < target and table[i][j] == 0:
                if len(oqueue) > 0:
                    si = oqueue.pop()
                    rcnt[i] += 1
                    rcnt[si] -= 1
                    print(i + 1, si + 1, j + 1)
                else:
                    zqueue.append(i)


t = int(input())
for _ in range(t):
    solve()
