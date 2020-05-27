from collections import deque
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def bfs(x,y, color):
    que = deque()
    visit[x][y] = 1
    que.append((x, y))

    while que:
        now_x, now_y = que.popleft()

        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]

            if next_x >= n or next_x < 0 or next_y >= n or next_y < 0:
                continue
            if visit[next_x][next_y]:
                continue
            if graph[next_x][next_y] != color:
                continue
            que.append((next_x, next_y))
            visit[next_x][next_y] = 1
def bfs_r_g(x,y):
    que = deque()
    visit[x][y] = 1
    que.append((x,y))

    while que:
        now_x, now_y = que.popleft()

        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]

            if next_x >= n or next_x < 0 or next_y >= n or next_y < 0:
                continue
            if visit[next_x][next_y]:
                continue
            if graph[next_x][next_y] == 'B':
                continue
            que.append((next_x,next_y))
            visit[next_x][next_y] = 1

def bfs_b(x,y):
    que = deque()
    visit[x][y] = 1
    que.append((x, y))

    while que:
        now_x, now_y = que.popleft()

        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]

            if next_x >= n or next_x < 0 or next_y >= n or next_y < 0:
                continue
            if visit[next_x][next_y]:
                continue
            if graph[next_x][next_y] != 'B':
                continue
            que.append((next_x, next_y))
            visit[next_x][next_y] = 1


n = int(input())

graph = []

for i in range(n):
    s = input()
    tmp = []
    for j in range(n):
        tmp.append(s[j])
    graph.append(tmp)
visit = [[0 for i in range(n)] for _ in range(n)]

cnt_r_g = 0

for i in range(n):
    for j in range(n):
        if visit[i][j]:
            continue
        cnt_r_g += 1
        if graph[i][j] == 'B':
            bfs_b(i,j)
        else:
            bfs_r_g(i,j)
visit = [[0 for i in range(n)] for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if visit[i][j]:
            continue
        cnt += 1
        bfs(i,j,graph[i][j])

print(cnt,cnt_r_g)