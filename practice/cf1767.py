n = int(input())
s = map(int, input())
zeroes = 0
ones = 0
for el in s:
    zeroes += 1 - el
    ones += el
print(" ".join(map(str, range(2**ones, 2**n - 2**zeroes + 2))))
