n = int(input())
l = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    qr = list(map(int, input().split()))
    if qr[0] == 1:
        l[qr[1] - 1] = qr[2]
    else:
        print(l[qr[1] - 1])
