def solve():
    n, a, b = tuple(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v, w = tuple(map(int, input().split()))
        graph[u].append((v, w))
        graph[v].append((u, w))
    tfb = {}
    queue = [(b, 0)]
    visited = [False] * (n + 1)
    while len(queue) > 0:
        cur, w = queue.pop(0)
        visited[cur] = True
        for node, wn in graph[cur]:
            if not visited[node]:
                wn ^= w
                tfb[wn] = True
                queue.append((node, wn))
    queue = [(a, 0)]
    visited = [False] * (n + 1)
    while len(queue) > 0:
        cur, w = queue.pop(0)
        if tfb.get(w) is not None:
            print("YES")
            return
        visited[cur] = True
        for node, wn in graph[cur]:
            if node == b and w ^ wn == 0:
                print("YES")
                return
            if node != b and not visited[node]:
                w ^= wn
                queue.append((node, w))
    print("NO")


t = int(input())
for _ in range(t):
    solve()
