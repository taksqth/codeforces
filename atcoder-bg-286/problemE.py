import sys

input = lambda: sys.stdin.readline().rstrip()


n = int(input())
a = list(map(int, input().split()))
graph = []
for i in range(n):
    graph.append(input())


dist = [[(float("inf"), 0)] * len(graph) for _ in range(len(graph))]
for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] == "Y":
            dist[i][j] = (1, -a[i] - a[j])
for i in range(len(graph)):
    dist[i][i] = (0, -a[i])
for k in range(len(graph)):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i == k:
                continue
            l = dist[i][k][0] + dist[k][j][0]
            souv = dist[i][k][1] + dist[k][j][1] + a[k]
            opt = (l, souv)
            if dist[i][j] > opt:
                dist[i][j] = opt

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    l, souv = dist[u][v]
    souv = -souv
    if l == float("inf"):
        sys.stdout.write("Impossible\n")
    else:
        sys.stdout.write(f"{l} {souv}\n")
