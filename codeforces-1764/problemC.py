def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = -1
    if n % 2 == 0:
        m = a[(n - 1) // 2] / 2 + a[n // 2] / 2
    else:
        m = a[n // 2]
    l = len([el for el in a if el < m])
    b = len([el for el in a if el > m])
    mm = len([el for el in a if el == m])
    if l < b:
        l += mm
    else:
        b += mm
    if l == 0:
        print(b // 2)
    else:
        print(l * b)


t = int(input())
for _ in range(t):
    solve()
