from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]

r,c = map(int,input().split())

graph = []
start = None
water = []
for i in range(r):
    info = input()
    tmp = []
    for j in range(c):
        if info[j] == '*':
            water.append((i,j))
        elif info[j] == 'S':
            start = (i,j)
        tmp.append(info[j])
    graph.append(tmp)

water_graph = [[987654321 for _ in range(c)] for _ in range(r)]

def water_bfs(water_point):
    que = deque()
    visit = [[0 for _ in range(c)] for _ in range(r)]
    for waterP in water_point:
        que.append(waterP)
        visit[waterP[0]][waterP[1]] = 1
        water_graph[waterP[0]][waterP[1]] = 0

    while que:
        now_x, now_y = que.popleft()

        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]

            if next_x >= r or next_x < 0 or next_y >= c or next_y < 0:
                continue
            if visit[next_x][next_y]:
                continue
            if graph[next_x][next_y] == 'D' or graph[next_x][next_y] == 'X':
                continue
            que.append((next_x,next_y))
            visit[next_x][next_y] = 1
            water_graph[next_x][next_y] = water_graph[now_x][now_y] + 1

water_bfs(water)
dist = [[0 for _ in range(c)] for _ in range(r)]
def bfs(sx,sy):
    que = deque()
    que.append((sx,sy))
    visit = [[0 for _ in range(c)] for _ in range(r)]
    visit[sx][sy] = 1

    while que:
        now_x, now_y = que.popleft()

        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]

            if next_x >= r or next_x < 0 or next_y >= c or next_y < 0:
                continue
            if visit[next_x][next_y]:
                continue
            if graph[next_x][next_y] == 'X':
                continue
            if graph[next_x][next_y] == 'D':
                return dist[now_x][now_y] + 1
            if water_graph[next_x][next_y] <= dist[now_x][now_y] + 1:
                continue
            que.append((next_x,next_y))
            visit[next_x][next_y] = 1
            dist[next_x][next_y] = dist[now_x][now_y] + 1
    return 'KAKTUS'

for row in water_graph:
    print(*row)
print()

print(bfs(start[0],start[1]))

for row in dist:
    print(*row)