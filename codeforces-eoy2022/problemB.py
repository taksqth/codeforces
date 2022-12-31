import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n, k = map(int, input().split())
    r = [0] * n
    for i in range(n):
        if i * k < n:
            r[i * k] = n - i
        elif (i - n // k - 1) * k + 1 < n:
            r[(i - n // k - 1) * k + 1] = i - n // k
        else:
            i -= 1
            break
    i += 1
    for j in range(n):
        if r[j] == 0:
            r[j] = i - n // k
            i += 1

    sys.stdout.write(" ".join(map(str, r)) + "\n")


t = int(input())
for _ in range(t):
    solve()
