import sys

input = lambda: sys.stdin.readline().rstrip()

_ = int(input())
a = input()

for i, el in enumerate(a):
    sys.stdout.write(el)
    if el == "n" and i < len(a) - 1 and a[i + 1] == "a":
        sys.stdout.write("y")
sys.stdout.write("\n")
