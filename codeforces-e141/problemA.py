import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    _ = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ret = [a[0]]
    removed = {0}
    for i, el in enumerate(a[1:]):
        if el != a[0]:
            ret.append(el)
            removed.add(i + 1)
            break
    if len(ret) == 1:
        sys.stdout.write("NO\n")
        return
    for i in range(len(a)):
        if i not in removed:
            ret.append(a[i])
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, ret)) + "\n")


t = int(input())
for _ in range(t):
    solve()
