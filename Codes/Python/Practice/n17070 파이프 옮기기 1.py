N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

# 출발지는 항상 (1,2)
# 0 : 가로 1: 세로 2: 대각선
cnt = 0
def track(pre_dir, pre_end):
    global cnt
    x = pre_end[0]
    y = pre_end[1]

    if x == N-1 and y == N-1:
        cnt += 1
        return

    if pre_dir == 0:
        if y+1 < N and graph[x][y+1] == 0:
            track(0,(x,y+1))
        if x+1 < N and y+1 < N:
            if graph[x+1][y] == 0 and graph[x][y+1] == 0 and graph[x+1][y+1] == 0:
                track(2,(x+1,y+1))
    elif pre_dir == 1:
        if x+1 < N and graph[x+1][y] == 0:
            track(1, (x+1, y))
        if y + 1 < N and x + 1 < N:
            if graph[x + 1][y] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y + 1] == 0:
                track(2, (x + 1, y + 1))
    else:
        if x+1<N and graph[x+1][y]==0:
            track(1,(x+1,y))
        if y+1<N and graph[x][y+1]==0:
            track(0,(x,y+1))
        if y + 1 < N and x + 1 < N:
            if graph[x + 1][y] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y + 1] == 0:
                track(2, (x + 1, y + 1))

track(0,(0,1))
print(cnt)