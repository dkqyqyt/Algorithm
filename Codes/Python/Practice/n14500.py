N,M = map(int,input().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

maxn = 0

visit = [[0 for _ in range(M)] for _ in range(N)]

def dfs(depth,x,y,ans,path):
    global maxn

    if depth == 3:
        # print(ans)
        # print(path)
        if ans > maxn:
            maxn = ans
        return
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if next_x >= N or next_x < 0 or next_y >= M or next_y < 0:
            continue
        if visit[next_x][next_y]:
            continue
        ans += graph[next_x][next_y]
        visit[next_x][next_y] = 1
        # path.append((next_x, next_y))
        dfs(depth+1,next_x,next_y,ans,path)
        ans -= graph[next_x][next_y]
        visit[next_x][next_y] = 0
        # path.pop()

def rest(x,y):
    global maxn
    for notUse in range(4):
        tmp = graph[x][y]
        cnt = 0
        for i in range(4):
            if i == notUse:
                continue
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x >= N or next_x < 0 or next_y >= M or next_y < 0:
                break
            tmp += graph[next_x][next_y]
            cnt += 1
        if cnt == 3:
            if tmp > maxn:
                maxn = tmp
for i in range(len(graph)):
    for j in range(len(graph[i])):
        visit[i][j] = 1
        dfs(0,i,j,graph[i][j],[])
        rest(i,j)
        visit[i][j] = 0

print(maxn)