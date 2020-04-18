from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N, L, R = map(int,input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

def bfs(sx,sy):
    que = deque()
    que.append((sx,sy))
    visit[sx][sy] = 1
    population = graph[sx][sy]
    locations = [(sx,sy)]

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if visit[nx][ny]:
                continue
            if abs(graph[x][y] - graph[nx][ny]) > R or abs(graph[x][y] - graph[nx][ny]) < L:
                continue
            visit[nx][ny] = 1
            que.append((nx,ny))
            population += graph[nx][ny]
            locations.append((nx,ny))

    new_population = population//len(locations)
    for loc in locations:
        graph[loc[0]][loc[1]] = new_population

turn = 0
while True:
    visit = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if not visit[i][j]:
                bfs(i,j)
                cnt += 1

    if cnt == N**2:
        break
    turn += 1

print(turn)