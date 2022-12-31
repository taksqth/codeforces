s = input()

d = [0] * 10
lzero = False
for l in s:
    if l == "0":
        if lzero:
            lzero = not lzero
            continue
        lzero = not lzero
    else:
        lzero = False
    d[int(l)] += 1

print(sum(d))
