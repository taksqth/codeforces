import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()


def solve():
    s = input()
    k = int(input())
    for i in range(len(s)):
        if s[i] == "0":
            break
    seqs = [s[:i], s[i:]]
    cnts = [Counter(seq) for seq in seqs]
    for i, cnt in enumerate(cnts):
        l = sum(cnt.values())
        if k >= l - 1:
            k -= l - 1
            seqs[i] = min(cnt.keys())
        else:
            while k > 0 and l > 0:
                mkey = max(cnt.keys())
                val = cnt[mkey]
                l -= min(val, k)
                cnt[mkey] -= min(val, k)
                k -= val
            break
    print(cnts[i])
    cnt = Counter(seqs[i]) - cnts[i]
    print(cnt)
    newseq = []
    for l in seqs[i]:
        if cnt[l] == 0:
            newseq.append(l)
        else:
            cnt[l] -= 1
    seqs[i] = "".join(newseq)
    sys.stdout.write("".join(seqs) + "\n")


t = int(input())
for _ in range(t):
    solve()
