S = []
while True:
    s = input()
    if s[:7] == ".......":
        break
    S.append(s)
print(" ".join(S))
