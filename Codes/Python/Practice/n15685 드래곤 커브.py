N = int(input())

dx = [0,-1,0,1]
dy = [1,0,-1,0]
graph = [[0 for _ in range(101)] for _ in range(101)]

def curve(max_g,now_g,move):
    if now_g == max_g:
        return move
    for i in range(len(move)-1,-1,-1):
        move.append((move[i]+1)%4)
    return curve(max_g,now_g + 1, move)

def brush(x,y,move):
    graph[x][y] = 1
    for dir in move:
        x = x + dx[dir]
        y = y + dy[dir]

        graph[x][y] = 1

def findsquare(graph):
    cnt = 0
    for i in range(100):
        for j in range(100):
            if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j+1] == 1:
                cnt += 1
    return cnt

for i in range(N):
    y,x,d,g = map(int,input().split())
    move = [d]
    move = curve(g,0,move)
    brush(x,y,move)

ans = findsquare(graph)

print(ans)