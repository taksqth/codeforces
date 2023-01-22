import heapq


def djikstra(graph, u):
    dist = [float("inf")] * len(graph)
    prev = [None] * len(graph)
    dist[u] = 0
    prev[u] = u
    q = []
    heapq.heappush(q, (dist[u], -a[u], u))
    while len(q) > 0:
        _, _, u = heapq.heappop(q)
        for v in graph[u]:
            if dist[u] + 1 < dist[v]:
                dist[v] = dist[u] + 1
                prev[v] = u
                heapq.heappush(q, (dist[v], -a[v], v))
    return prev
