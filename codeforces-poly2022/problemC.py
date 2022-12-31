def solve():
    _ = int(input())
    s = input()

    ret = []
    cnt_same = 1
    last = 2
    for i, el in enumerate(s):
        if last != el:
            last = el
            cnt_same = 1
        else:
            cnt_same += 1
        ret.append(i - cnt_same + 2)
    print(" ".join(map(str, ret)))


t = int(input())
for _ in range(t):
    solve()
