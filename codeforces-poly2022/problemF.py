n = input()
cdamage = [0] * (2 * 10**5)
for i in range(n):
    inst = list(map(int, input().split()))
    if inst[0] == 2:
        cdamage[i] = cdamage[max(0, i)] + inst[1]
    if inst[0] == 3:
        cdamage[i] = 2 * cdamage[max(0, i)]
