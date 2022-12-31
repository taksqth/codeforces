import sys

for line in sys.stdin:
    l = list(map(int, line.split()))
    n = l[0]
    l = l[1:]
    s = set()
    if len(l) == 1:
        print("Jolly")
        continue
    for i in range(1, n):
        diff = abs(l[i] - l[i - 1])
        if diff > 0 and diff < n:
            s.add(diff)
    if len(s) == n - 1:
        print("Jolly")
    else:
        print("Not Jolly")
