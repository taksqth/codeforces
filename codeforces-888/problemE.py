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
    cc = [0] * n
    p = list(map(int, input().split()))
    for el in p:
        c[el-1] = 0
    depends_on = [set() for i in range(n)]
    is_used_for = [set() for i in range(n)]
    for i in range(n):
        e = list(map(int, input().split()))
        e = e[1:]
        if len(e) == 0:
            cc[i] = c[i]
        for el in e:
            depends_on[i].add(el-1)
            is_used_for[el-1].add(i)
    
    stack = []
    for i in range(n):
        if len(depends_on[i]) == 0:
            stack.append(i)
    
    while len(stack) > 0:
        el = stack.pop()
        for i in is_used_for[el]:
            depends_on[i].remove(el)
            cc[i] += min(c[el], cc[el])
            if len(depends_on[i]) == 0:
                stack.append(i)

    min_cost = []
    for i in range(n):
        min_cost.append(min(c[i], cc[i]))
    sys.stdout.write(str(' '.join(map(str, min_cost))) + '\n')

t = int(input())
for i in range(t):
    solve(i+1)
