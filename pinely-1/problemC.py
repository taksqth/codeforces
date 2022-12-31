def solve_case():
    n = int(input())
    m = [list(map(int, input())) for _ in range(n)]
    sets = [set() for _ in range(n)]
    k = 1
    indegree = [sum(m[j][i] for j in range(n)) for i in range(n)]
    queue = [i for i in range(n) if indegree[i] == 0]
    while len(queue) > 0:
        cur = queue.pop(0)
        sets[cur].add(k)
        k += 1
        for i in range(n):
            if m[i][cur] == 1:
                for el in sets[i]:
                    sets[cur].add(el)
        for i in range(n):
            if m[cur][i] == 1:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
    for i in range(n):
        print(str(len(sets[i])) + " " + " ".join(map(str, sets[i])))


t = int(input())
for _ in range(t):
    solve_case()
