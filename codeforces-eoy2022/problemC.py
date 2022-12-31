import sys

input = lambda: sys.stdin.readline().rstrip()


def primes_to(n):
    check = [True] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if check[i]:
            primes.append(i)
        j = 2
        while i * j < n + 1:
            check[i * j] = False
            j += 1
    return primes


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    seen = set()
    for el in a:
        if el in seen:
            sys.stdout.write("NO\n")
            return
        seen.add(el)

    primes = primes_to(100)
    for prime in primes:
        check = [0] * prime
        for el in a:
            check[el % prime] += 1
        if all([el > 1 for el in check]):
            sys.stdout.write("NO\n")
            return
    sys.stdout.write("YES\n")


t = int(input())
for _ in range(t):
    solve()
