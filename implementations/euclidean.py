def gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 1:
        return b
    return gcd(a, b % a)
