n = int(input())
l = list(map(int, input().split()))

leftmax = []
cmax = float("-inf")
for el in l:
    leftmax.append(cmax)
    if el > cmax:
        cmax = el

rightmin = []
cmin = float("inf")
for el in l[::-1]:
    rightmin.append(cmin)
    if el < cmin:
        cmin = el
rightmin = rightmin[::-1]

ret = []
for i, el in enumerate(l):
    if el > leftmax[i] and el < rightmin[i]:
        ret.append(el)
print(" ".join(map(str, ret)))
