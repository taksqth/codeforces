import sys

input = lambda: sys.stdin.readline().rstrip()

from random import randint
 
RANDOM = randint(1, 10 ** 9)
 
class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

DEBUG=False

def solve(case=0):
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a

    ns = [False] * (n + 1)
    target = 0
    for i in range(1, n):
        if a[i] - a[i-1] > n:
            target = a[i] - a[i-1]
        if a[i] - a[i-1] <= n:
            if ns[a[i] - a[i-1]]:
                target = a[i] - a[i-1]
            ns[a[i] - a[i-1]] = True
    if DEBUG: print(f"Case #{case}: {n, a, ns, target}")

    missing = []
    for i in range(1, n+1):
        if not ns[i]:
            missing.append(i)
    
    if len(missing) == 1 or (len(missing) == 2 and sum(missing) == target):
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")




t = int(input())
for i in range(t):
    solve(i+1)
