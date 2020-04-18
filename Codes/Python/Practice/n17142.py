from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N, M = map(int,input().split())

graph = []
viruses = []
for i in range(N):
    v_list = list(map(int,input().split()))
    for idx, num in enumerate(v_list):
        if num == 2:
            viruses.append((i,idx))
    graph.append(v_list)
used = [0 for _ in range(len(viruses))]
def infection(mygraph):
    for i in range(len(mygraph)):
        for j in range(len(mygraph[i])):
            if mygraph[i][j] == 0 and graph[i][j] == 0:
                return False
    return True

def bfs(candidates):
    que = deque()
    visit = [[0 for _ in range(N)] for _ in range(N)]
    new_graph = [[0 for _ in range(N)] for _ in range(N)]

    for can in candidates:
        que.append(can)
        visit[can[0]][can[1]] = 1
    maxn = 0
    while que:
        x,y = que.popleft()

        for i in range(4):
            nextx = x + dx[i]
            nexty = y + dy[i]

            if nextx >= N or nextx < 0 or nexty >= N or nexty < 0:
                continue
            if visit[nextx][nexty]:
                continue
            if graph[nextx][nexty]== 1:
                continue
            if graph[nextx][nexty] == 2:
                new_graph[nextx][nexty] = new_graph[x][y]
                if new_graph[nextx][nexty] > maxn:
                    maxn = new_graph[nextx][nexty]
                visit[nextx][nexty] = 1
                que.append((nextx, nexty))
                continue
            new_graph[nextx][nexty] = new_graph[x][y] + 1
            if new_graph[nextx][nexty] > maxn:
                maxn = new_graph[nextx][nexty]
            visit[nextx][nexty] = 1
            que.append((nextx,nexty))
    bool = infection(new_graph)
    if bool:
        return maxn
    else:
        return 987654321

minn = 987654321
def track(depth,path):
    global minn
    if depth == M:
        time = bfs(path)
        if time < minn:
            # print(path, time)
            minn = time
        return
    for i in range(len(viruses)):
        if used[i]:
            continue
        used[i] = 1
        path.append(viruses[i])
        track(depth+1,path)
        used[i] = 0
        path.pop()

track(0,[])
if minn == 987654321:
    print(-1)
else:
    print(minn)
