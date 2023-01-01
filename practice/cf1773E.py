import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()


def solve_pqueue():
    n = int(input())
    ts = []
    c = 0
    for _ in range(n):
        c += 1
        _, *a = map(int, input().split())
        ts.append(a)
    nts = []

    s = 0
    for t in ts:
        nts.append([t[0]])
        for i in range(1, len(t)):
            if t[i] < t[i - 1]:
                s += 1
                nts.append([t[i]])
            else:
                nts[-1].append(t[i])
    ts = nts

    pqueue = []
    for i, t in enumerate(ts):
        for el in t:
            pqueue.append((el, i))

    heapq.heapify(pqueue)
    seen = [False] * len(ts)
    _, i = heapq.heappop(pqueue)
    seen[i] = True
    while len(pqueue) > 0:
        _, ni = heapq.heappop(pqueue)
        if ni != i and seen[ni]:
            s += 1
        seen[ni] = True
        i = ni
    sys.stdout.write(f"{s} {c+s-1}\n")


def solve_sortindex():
    n = int(input())
    ts = []
    c = 0
    for _ in range(n):
        c += 1
        _, *a = map(int, input().split())
        ts.append([[el, 0] for el in a])
    l = [el for t in ts for el in t]
    l.sort(key=lambda el: el[0])

    s = 0
    for i, el in enumerate(l):
        el[1] = i
    for t in ts:
        for i in range(1, len(t)):
            if t[i][1] != t[i - 1][1] + 1:
                s += 1

    sys.stdout.write(f"{s} {c+s-1}\n")


solve_sortindex()
