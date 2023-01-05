import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    _ = int(input())
    x = list(map(int, input().split()))

    cnt = Counter(x)

    queue = []
    for i in range(n):
        if b[i] > a[i]:
            sys.stdout.write("NO\n")
            return
        elif b[i] == a[i]:
            while len(queue) > 0 and queue[-1] < b[i]:
                queue.pop()
            continue
        else:
            while len(queue) > 0 and queue[-1] < b[i]:
                queue.pop()
            if len(queue) == 0 or queue[-1] != b[i]:
                if cnt[b[i]] == 0:
                    sys.stdout.write("NO\n")
                    return
                cnt[b[i]] -= 1
                queue.append(b[i])
    sys.stdout.write("YES\n")


t = int(input())
for _ in range(t):
    solve()
