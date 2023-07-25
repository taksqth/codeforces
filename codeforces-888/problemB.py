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
    sa = sorted(a)

    for i in range(len(a)):
        if a[i] % 2 != sa[i] % 2:
            sys.stdout.write("NO\n")
            return
    sys.stdout.write("YES\n")

t = int(input())
for i in range(t):
    solve(i+1)
