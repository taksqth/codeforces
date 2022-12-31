import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    _, m = map(int, input().split())
    a = list(map(int, input().split()))

    t = sum(a) + 1
    a.sort()
    a = [0] + a
    l = 0
    r = len(a) - 1
    lb = True
    while l < r:
        if a[l] + a[r] > m:
            r -= 1
            t += 1
            lb = False
        elif lb:
            l += 1
            lb = False
        else:
            r -= 1
            lb = True
    sys.stdout.write(str(t) + "\n")


solve()
