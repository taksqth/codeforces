def solve():
    _ = int(input())
    s = input()
    out = []
    last_one = s[0] == "1"
    for l in s[1:]:
        if l == "1":
            last_one = not last_one
            if not last_one:
                out.append("-")
                continue
        out.append("+")
    print("".join(out))


t = int(input())
for _ in range(t):
    solve()
