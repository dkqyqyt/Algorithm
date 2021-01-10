dx = [-1,-1,-1,0,0,1,1,1]
dy = [1,0,-1,1,-1,1,0,-1]

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]
tcs = int(input())

for tc in range(tcs):
    length = int(input())

    graph = [[0 for _ in range(length)] for _ in range(length)]
    visit = [[0 for _ in range(length)] for _ in range(length)]
    sx,sy = map(int,input().split())
    tx,ty = map(int,input().split())

    que = [(sx,sy)]
    visit[sx][sy] = 1

    while que:
        x,y = que.pop(0)

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= length or nx < 0 or ny >= length or ny < 0:
                continue
            if visit[nx][ny]:
                continue

            graph[nx][ny] = graph[x][y] + 1
            visit[nx][ny] = 1

            que.append((nx,ny))

    # for row in graph:
    #     print(*row)
    print(graph[tx][ty])
