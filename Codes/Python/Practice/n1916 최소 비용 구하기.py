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
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))
start, destination = map(int,input().split())

dist = [INF for _ in range(n+1)]

dijkstra(start)
print(dist[destination])