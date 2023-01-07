import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
l = []
for _ in range(n):
    l.insert(0, input())
for i in range(n):
    sys.stdout.write(l[i] + "\n")
