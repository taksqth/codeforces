def hash(R, X, Y):
    V = 0
    for i in range(0, len(R)):
        V = (V * X + R[i]) % Y
    return V


def countingSort(arr, exp1, b=10):
    n = len(arr)
    output = [0] * n
    count = [0] * b

    for i in range(n):
        index = arr[i] // exp1
        count[index % b] += 1

    for i in range(1, b):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % b] - 1] = arr[i]
        count[index % b] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr, b=10):
    max1 = max(arr)

    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp, b)
        exp *= b


def solve_case():
    N = int(input())
    A, B, C = tuple(map(int, input().split()))
    X, Y = tuple(map(int, input().split()))

    S = [A]
    for i in range(1, N):
        S.append((S[i - 1] * B + A) % C)
    radixSort(S, b=10**6)

    print(hash(S, X, Y))


T = int(input())
for _ in range(T):
    solve_case()
