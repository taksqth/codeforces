import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    _ = input()
    l = list(map(int, input().split()))
    ret = 0
    while True:
        for i in range(1, len(l)):
            if l[i - 1] % 2 == l[i] % 2:
                l.insert(i - 1, l[i - 1] * l[i])
                del l[i]
                del l[i]
                ret += 1
                break
        else:
            break
    sys.stdout.write(str(ret) + "\n")


t = int(input())
for _ in range(t):
    solve()
