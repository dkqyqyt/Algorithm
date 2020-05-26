import heapq

def dijkstra(start):
    que = []
    heapq.heappush(que,(0,start))
    dist[start] = 0

    while que:
        now_dist, now = heapq.heappop(que)

        for next_node, weight in graph[now]:
            if dist[next_node] > dist[now] + weight:
                dist[next_node] = dist[now] + weight
                heapq.heappush(que,(dist[next_node], next_node))

INF = 987654321
n, e = map(int,input().split())
graph = [[] for _ in range(n+1)]
dist = [INF for _ in range(n+1)]

for i in range(e):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))

start = 1
destination = n
s1, s2 = map(int,input().split())

s1_to_s2 = 0
dijkstra(start)
s1_to_s2 += dist[s1]
dist = [INF for _ in range(n+1)]
dijkstra(s1)
s1_to_s2 += dist[s2]
dist = [INF for _ in range(n+1)]
dijkstra(s2)
s1_to_s2 += dist[destination]

dist = [INF for _ in range(n+1)]
s2_to_s1 = 0
dijkstra(start)
s2_to_s1 += dist[s2]
dist = [INF for _ in range(n+1)]
dijkstra(s2)
s2_to_s1 += dist[s1]
dist = [INF for _ in range(n+1)]
dijkstra(s1)
s2_to_s1 += dist[destination]

ans = min(s1_to_s2, s2_to_s1)

if ans >= INF:
    print(-1)
else:
    print(ans)