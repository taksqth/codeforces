def dp_factor_parity(limit=200005):
    def prime_up_to(n):
        notprime = [False] * (limit + 1)
        primes = []
        for i in range(2, n + 1):
            if not notprime[i]:
                primes.append(i)
            for j in range(i, n + 1, i):
                notprime[j] = True
        return primes

    primes = prime_up_to(limit)
    dp = [0] * limit
    dp[0] = 0
    dp[1] = 0
    for i in range(2, limit):
        even = False
        ci = i
        for prime in primes:
            if prime**2 > i:
                break
            cnt = 0
            while ci % prime == 0:
                ci //= prime
                cnt += 1
            if cnt % 2 == 1:
                even = True
                break
        if even or ci > 1:
            dp[i] = 1
    return dp


print(sum(map(lambda el: 1 - el, dp_factor_parity(200000))))
