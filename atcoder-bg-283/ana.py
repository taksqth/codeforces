l = [
    1,
    14857549,
    24,
    98717693,
    1260,
]

ret = 1
for el in l:
    ret *= el
print(ret % (10**9 + 7))
