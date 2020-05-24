import heapq

v, e = map(int,input().split())
start = int(input())

graph = [[] for _ in range(v+1)]
dist = [987654321]*(v+1)

for i in range(e):
    s,e,w = map(int,input().split())

    graph[s].append((w,e))

def bfs(start):
    que = []
    heapq.heappush(que, (0,start))
    dist[start] = 0

    while que:
        now_d, now = heapq.heappop(que)

        for weight,next_node  in graph[now]:
            if dist[next_node] > dist[now] + weight:
                dist[next_node] = dist[now] + weight
                heapq.heappush(que, (dist[next_node], next_node))

bfs(start)

for i in range(1, len(dist)):
    if dist[i] == 987654321:
        print('INF')
    else:
        print(dist[i])