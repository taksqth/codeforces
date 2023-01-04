import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    flips = 0

    pqueue = []
    s = 0
    for i in range(m - 1, 0, -1):
        heapq.heappush(pqueue, -a[i])
        s += a[i]
        while s > 0:
            s += 2 * heapq.heappop(pqueue)
            flips += 1

    pqueue = []
    s = 0
    for i in range(m, n):
        heapq.heappush(pqueue, a[i])
        s += a[i]
        while s < 0:
            s -= 2 * heapq.heappop(pqueue)
            flips += 1

    sys.stdout.write(str(flips) + "\n")


t = int(input())
for _ in range(t):
    solve()
