def primes_up_to(n):
    notprime = [False] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if not notprime[i]:
            primes.append(i)
        for j in range(i, n + 1, i):
            notprime[j] = True
    return primes


print(primes_up_to(50000))
