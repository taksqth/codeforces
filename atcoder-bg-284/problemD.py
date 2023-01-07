import sys
import math

input = lambda: sys.stdin.readline().rstrip()

limit = math.floor((9 * 10**18) ** (1.0 / 3.0))
valid = [True] * limit
primes = []
for i in range(2, limit):
    if valid[i]:
        primes.append(i)
        for j in range(i * i, limit, i):
            valid[j] = False


def solve():
    n = int(input())
    for prime in primes:
        if n % prime == 0:
            n //= prime
            if n % prime == 0:
                sys.stdout.write(f"{prime} {n//prime}\n")
            else:
                sys.stdout.write(f"{int(math.sqrt(n))} {prime}\n")
            return


t = int(input())
for _ in range(t):
    solve()
