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
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    if DEBUG: print(f"Case #{case}: {n, k}")

    if k == 1:
        sys.stdout.write('YES\n')
        return
    if n == 1 and k > 1:
        sys.stdout.write('NO\n')
        return
    
    if c[0] == c[n-1]:
        cnt = 0
        if cnt == k-2:
            sys.stdout.write('YES\n')
            return
        for el in c[1:n-1]:
            if el == c[0]:
                cnt += 1
            if cnt == k-2:
                sys.stdout.write('YES\n')
                return
    
    if c[0] != c[n-1]:
        i = 1
        cnt = 0
        while i < n:
            if c[i] == c[0]:
                cnt += 1
            i += 1
            if cnt == k-1:
                break
        cnt = 0
        while i < n:
            if c[i] == c[n-1]:
                cnt += 1
            i += 1
            if cnt == k:
                sys.stdout.write('YES\n')
                return
    
    sys.stdout.write('NO\n')


t = int(input())
for i in range(t):
    solve(i+1)
