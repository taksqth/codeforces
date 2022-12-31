import sys

input = lambda: sys.stdin.readline().rstrip()

def test():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    

t = int(input())
for _ in range(t):
    solve()
