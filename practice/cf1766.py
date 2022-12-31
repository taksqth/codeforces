import os, sys
from io import BytesIO

sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
input = lambda: sys.stdin.readline().decode().strip()

valid = [True] * 3164
valid[0] = valid[1] = False
mind = [i for i in range(10**7 + 1)]
for i in range(2, 3164):
    if valid[i]:
        j = 1
        while i * j < 10**7 + 1:
            mind[i * j] = i
            j += 1
    j = 2
    while i * j < 3164:
        valid[i * j] = False
        j += 1


def factorize(n):
    fact = set()
    while n > 1:
        fact.add(mind[n])
        n //= mind[n]
    return fact


n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    diff = abs(x - y)
    if diff == 1:
        sys.stdout.write("-1\n")
    else:
        factors = factorize(diff)
        value = min(
            [
                factor - max((x - 1) % factor + 1, (y - 1) % factor + 1)
                for factor in factors
            ]
        )
        sys.stdout.write(str(value) + "\n")
