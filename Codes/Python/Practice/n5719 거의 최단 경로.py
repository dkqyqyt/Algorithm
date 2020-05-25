import heapq

def dijkstra(start):
    que = []
    heapq.heappush(que,(0,start))
    dist[start] = 0

    while que:
        w, now = heapq.heappop(que)
        for i in range(n):
            if graph[now][i] == 0:
                continue
            next_node = i
            weight = graph[now][i]

            if dist[next_node] == dist[now]+weight:
                pre_node[next_node].append(now)
            elif dist[next_node] > dist[now] + weight:
                pre_node[next_node].clear()
                pre_node[next_node].append(now)
                dist[next_node] = dist[now] + weight
                heapq.heappush(que,(dist[next_node],next_node))

while True:
    n, m = map(int,input().split())
    if n == 0 and m == 0:
        break

    start, dest = map(int,input().split())

    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        s,e,w = map(int,input().split())
        graph[s][e] = w
    dist = [987654321 for _ in range(n)]
    pre_node = [[] for _ in range(n)]
    delete = [0 for _ in range(n)]

    dijkstra(start)
    stack = [dest]
    while stack:
        route = stack.pop()

        for i in range(len(pre_node[route])):
            stack.append(pre_node[route][i])
            graph[pre_node[route][i]][route] = 0

    dist = [987654321 for _ in range(n)]
    dijkstra(start)

    if dist[dest] == 987654321:
        print(-1)
    else:
        print(dist[dest])

