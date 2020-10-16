import heapq

dx = [1,-1,0,0]
dy = [0,0,1,-1]
tc = 1
while True:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int,input().split())) for _ in range(n)]
    loses = [[987654321 for _ in range(n)] for _ in range(n)]

    que = []
    heapq.heappush(que,(graph[0][0],0,0))
    loses[0][0] = graph[0][0]
    while que:
        lose, x, y = heapq.heappop(que)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue

            if loses[nx][ny] > lose + graph[nx][ny]:
                loses[nx][ny] = lose + graph[nx][ny]
                heapq.heappush(que, (loses[nx][ny], nx,ny))
    print('Problem ' + str(tc) + ': ' + str(loses[n-1][n-1]))
    tc += 1