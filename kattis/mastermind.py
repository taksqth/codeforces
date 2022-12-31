from collections import Counter

n, code, guess = tuple(input().split())
n = int(n)

r = 0
ccnt = Counter()
gcnt = Counter()
for i in range(n):
    if code[i] == guess[i]:
        r += 1
    ccnt[code[i]] += 1
    gcnt[code[i]] += 1

s = 0
for k, cnt in gcnt.items():
    s += min(ccnt[k], cnt)

print(r, s - r)
