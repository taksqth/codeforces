def counting_sort(l, exp, b=10):
    n = len(l)
    ret = [0] * n
    cnt = [0] * b
    for i in range(n):
        index = l[i] // exp
        cnt[index % b] += 1
    for i in range(1, b):
        cnt[i] += cnt[i - 1]
    for i in range(n - 1, -1, -1):
        index = l[i] // exp
        ret[cnt[index % b] - 1] = l[i]
        cnt[index % b] -= 1
    i = 0
    for i in range(n):
        l[i] = ret[i]


def radix_sort(l, b=10):
    m = max(l)
    exp = 1
    while m / exp >= 1:
        counting_sort(l, exp, b)
        exp *= b


l = [
    234234,
    342346453,
    45637,
    324623,
    6326237,
    436,
    7374,
    74327234,
    2346,
    34634,
    523453,
]
radix_sort(l)
print(l)
