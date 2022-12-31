def solve_case():
    n, a, b = tuple(map(int, input().split()))
    if n == a and n == b:
        print('Yes')
    elif n - 2 >= a + b:
        print('Yes')
    else:
        print('No')

t = int(input())
for i in range(t):
    solve_case()