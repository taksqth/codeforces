n, p = tuple(map(int, input().split()))


def modinv0(x, p):
    "return the inverse of x in Z/pZ (x nonzero)"
    return pow(x, p - 2, p)


tabfact = [1] * (n + 1)
tabfactinv = [1] * (n + 1)
for k in range(2, n + 1):
    tabfact[k] = (k * tabfact[k - 1]) % p
    tabfactinv[k] = modinv0(tabfact[k], p)

ret = 0
for i in range((n + 1) // 2):
    bot = (n + 1) // 2
    top = n // 2 + i
    for j in range(max(1, i)):
        choose = tabfact[max(0, i - 1)] * tabfactinv[j] * tabfactinv[max(0, i - 1) - j]
        ret += choose * (top - bot + 1) * tabfact[n - i + j - 2]
        ret %= p
print((ret * n) % p)
