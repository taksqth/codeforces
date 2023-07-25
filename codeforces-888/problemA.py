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
    _, m, k, H = map(int, input().split())
    if DEBUG: print(f"Case #{case}: {m, k, H}")
    h = list(map(int, input().split()))
    cnt = 0
    for el in h:
        if el != H and abs(el - H) % k == 0 and abs(el - H) // k < m:
            if DEBUG: print(el, H, abs(el-H), abs(el - H) // k)
            cnt += 1
    sys.stdout.write(str(cnt) + '\n')
    if DEBUG: print()
            


t = int(input())
for _ in range(t):
    solve(t)
