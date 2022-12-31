def solve():
    _ = input()
    s = input()
    max = 0
    for c in s:
        diff = ord(c) - ord("a") + 1
        if diff > max:
            max = diff
    print(max)


t = int(input())
for _ in range(t):
    solve()
