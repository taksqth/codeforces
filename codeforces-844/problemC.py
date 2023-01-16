import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n = int(input())
    s = input()

    cnt = [[0, l] for l in "abcdefghijklmnopqrstuvwxyz"]
    for l in s:
        cnt[ord(l) - ord("a")][0] += 1
    unused = []
    for i in range(26):
        if cnt[i][0] == 0:
            unused.append(chr(i + ord("a")))
    cnt.sort()
    minswaps = float("inf")
    mini = 0
    for i in range(1, 27):
        diff = 0
        if n % i != 0:
            continue
        for j in range(25, 25 - i, -1):
            diff += max(0, n // i - cnt[j][0])
        if diff < minswaps:
            minswaps = diff
            mini = i
    toinc = {l: max(0, n // mini - cnt) for cnt, l in cnt[-mini:]}
    stack = []
    for key, value in toinc.items():
        for i in range(value):
            stack.append(key)
    todec = {l: max(0, cnt - n // mini) for cnt, l in cnt[-mini:]}
    for i in range(26 - mini):
        todec[cnt[i][1]] = cnt[i][0]
    ret = []
    for l in s:
        if todec.get(l) is not None and todec[l] > 0:
            ret.append(stack.pop())
            todec[l] -= 1
        else:
            ret.append(l)
    sys.stdout.write(str(minswaps) + "\n")
    sys.stdout.write("".join(ret) + "\n")


t = int(input())
for _ in range(t):
    solve()
