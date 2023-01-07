import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * n


def dfs(v):
    visited[v] = True
    stack = [v]
    while len(stack) > 0:
        v = stack.pop()
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                stack.append(u)


ret = 0
for i in range(n):
    if not visited[i]:
        ret += 1
        dfs(i)
sys.stdout.write(str(ret) + "\n")
