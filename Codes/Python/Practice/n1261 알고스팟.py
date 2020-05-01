from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]

n, m = map(int,input().split())

graph = []

def bfs():
    que = deque()
    que.append((0,0))
    visit[0][0] = 1

    while que:
        now_x, now_y = que.popleft()
        # print(now_x,now_y)
        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            if next_x >= m or next_x < 0 or next_y >= n or next_y < 0:
                continue
            if not visit[next_x][next_y]:
                if graph[next_x][next_y] == 1:
                    que.append((next_x,next_y))
                    visit[next_x][next_y] = 1
                    wall[next_x][next_y] = wall[now_x][now_y] + 1
                else:
                    que.append((next_x,next_y))
                    visit[next_x][next_y] = 1
                    wall[next_x][next_y] = wall[now_x][now_y]
            else:
                if graph[next_x][next_y] == 1:
                    if wall[next_x][next_y] > wall[now_x][now_y] + 1:
                        wall[next_x][next_y] = wall[now_x][now_y] + 1
                        que.append((next_x,next_y))
                else:
                    if wall[next_x][next_y] > wall[now_x][now_y]:
                        wall[next_x][next_y] = wall[now_x][now_y]
                        que.append((next_x,next_y))

for i in range(m):
    data = input()
    tmp = []
    for j in range(n):
        tmp.append(int(data[j]))
    graph.append(tmp)
visit = [[0 for _ in range(n)] for _ in range(m)]
# for row in visit:
#     print(*row)
wall = [[0 for _ in range(n)] for _ in range(m)]
bfs()
# for row in wall:
#     print(*row)
print(wall[m-1][n-1])