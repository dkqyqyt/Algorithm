from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N, M = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]

def dfs(sx,sy,num):
    stack = []
    stack.append((sx,sy))
    visit[sx][sy] = 1
    graph[sx][sy] = num

    while stack:
        nx,ny = stack.pop()
        for i in range(4):
            next_x = nx + dx[i]
            next_y = ny + dy[i]

            if next_x >= N or next_x < 0 or next_y >= M or next_y < 0:
                continue
            if graph[next_x][next_y] == 0:
                continue
            if visit[next_x][next_y]:
                continue

            graph[next_x][next_y] = num
            visit[next_x][next_y] = 1
            stack.append((next_x,next_y))

num = 1

for i in range(N):
    for j in range(M):
        if visit[i][j] or graph[i][j] == 0:
            continue
        dfs(i,j,num)
        num += 1

num_of_island = num - 1

# print(num_of_island)
# for row in graph:
#     print(*row)
# print()

is_dist = [[987654321 for _ in range(num_of_island+1)] for _ in range(num_of_island+1)]

def dist_find(x,y,island_num):
    que = deque()
    que.append((x,y,-1))
    dist = [[0 for _ in range(M)] for _ in range(N)]

    while que:
        now_x, now_y, pre_move = que.popleft()

        for i in range(4):
            if pre_move == -1 or i == pre_move:
                next_x = now_x + dx[i]
                next_y = now_y + dy[i]

                if next_x >= N or next_x < 0 or next_y >= M or next_y < 0:
                    continue
                if graph[next_x][next_y] == island_num:
                    continue
                if graph[next_x][next_y] == 0:
                    que.append((next_x,next_y,i))
                    dist[next_x][next_y] = dist[now_x][now_y] + 1
                    continue
                if dist[now_x][now_y] < 2:
                    continue
                next_island = graph[next_x][next_y]
                if is_dist[island_num][next_island] > dist[now_x][now_y]:
                    is_dist[island_num][next_island] = dist[now_x][now_y]

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 0:
            continue
        dist_find(i,j,graph[i][j])

# for row in is_dist:
#     print(*row)

ddist = []

for i in range(1,num_of_island+1):
    for j in range(i+1,num_of_island+1):
        ddist.append((i,j))

# print(paths)
ggraph = [[] for _ in range(num_of_island+1)]

def bfs(sn):
    visit = [0 for _ in range(num_of_island+1)]
    que = deque()
    que.append(sn)
    visit[sn] = 1

    while que:
        node = que.popleft()

        for i in range(len(ggraph[node])):
            nextNode = ggraph[node][i]
            if visit[nextNode]:
                continue
            que.append(nextNode)
            visit[nextNode] = 1
    for i in range(1,num_of_island+1):
        if visit[i] == 0:
            return False
    return True

total_dist = 987654321

def track(depth, idx, path, dist):
    global total_dist
    # print(path)
    if depth == num_of_island-1:
        # print(path)
        # print(ggraph)
        if bfs(1):
            # print(dist)

            if total_dist > dist:
                # print(path)
                total_dist = dist
        return

    for i in range(idx+1, len(ddist)):
        s,e = ddist[i]
        if is_dist[s][e] == 987654321:
            continue
        ggraph[s].append(e)
        ggraph[e].append(s)
        dist += is_dist[s][e]
        path.append(ddist[i])
        track(depth+1, i, path,dist)
        ggraph[s].pop()
        ggraph[e].pop()
        dist -= is_dist[s][e]
        path.pop()

track(0,-1,[],0)
if total_dist == 987654321:
    print(-1)
else:
    print(total_dist)