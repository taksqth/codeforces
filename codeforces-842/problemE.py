import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

limit = 3 * 10**6 + 1
fact = [0] * limit
ifact = [0] * limit
fact[0] = fact[1] = 1

for i in range(2, limit):
    fact[i] = (i * fact[i - 1]) % m

ifact[-1] = pow(fact[-1], m - 2, m)
for i in range(limit - 1, -1, -1):
    ifact[i - 1] = (i * ifact[i]) % m


def f1(n, p):
    return (fact[2 * n] + fact[2 * n] - fact[n] - 1) % p


def f2(n, p):
    ret = (2 * pow(fact[2 * n], 2, p) * ifact[n]) % p
    for i in range(n + 1):
        ret -= (
            pow(fact[n], 4, p)
            * fact[2 * n - i]
            * pow(ifact[i], 2, p)
            * pow(ifact[n - i], 3, p)
        ) % p
    return (ret - f1(n, p) - 1) % p


def f3(n, p):
    return (fact[3 * n] - f2(n, p) - f1(n, p) - 1) % p


def r(n, p):
    return (f1(n, p) + 2 * f2(n, p) + 3 * f3(n, p)) % p


sys.stdout.write(str(r(n, m)) + "\n")
