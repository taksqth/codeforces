import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
t = input()


def ci(c):
    return ord(c) - ord("a")


p1 = 31
m1 = 999119999
p2 = 53
m2 = 1000992299

hr1 = 0
hr2 = 0
h1 = 0
h2 = 0
pp1 = 1
pp2 = 1
for i in range(n):
    hr1 += ci(t[n - i - 1]) * pp1
    hr1 %= m1
    hr2 += ci(t[n - i - 1]) * pp2
    hr2 %= m2
    h1 += ci(t[n + i]) * pp1
    h1 %= m1
    h2 += ci(t[n + i]) * pp2
    h2 %= m2
    pp1 *= p1
    pp1 %= m1
    pp2 *= p2
    pp2 %= m2

i = 0
pp1 = pow(p1, n - 1, m1)
pp2 = pow(p2, n - 1, m2)
ppi1 = 1
ppi2 = 1
while i < n and (h1 != hr1 or h2 != hr2):
    h1 = (h1 - ci(t[n + i]) * ppi1 + ci(t[i]) * ppi1) % m1
    h2 = (h2 - ci(t[n + i]) * ppi2 + ci(t[i]) * ppi2) % m2
    hr1 = ((hr1 - ci(t[i]) * pp1) * p1 + ci(t[n + i])) % m1
    hr2 = ((hr2 - ci(t[i]) * pp2) * p2 + ci(t[n + i])) % m2
    ppi1 *= p1
    ppi1 %= m1
    ppi2 *= p2
    ppi2 %= m2
    i += 1
if i < n:
    s = t[i : i + n]
    sys.stdout.write(t[::-1] + "\n")
    sys.stdout.write(str(i) + "\n")
else:
    sys.stdout.write("-1\n")
