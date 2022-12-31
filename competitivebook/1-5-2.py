p = input()
t = input()
l = []
for i in range(len(p)-len(t)):
    if p[i:i+len(t)] == t:
        l.append(i)
print(l)
