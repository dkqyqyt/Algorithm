dx = [1,-1,0,0]
dy = [0,0,1,-1]

def find(x,y):
    color = graph[x][y]
    x_cnt = 1
    y_cnt = 1
    for i in range(x+1,n):
        if graph[i][y] == color:
            x_cnt += 1
        else:
            break
    for i in range(x-1,-1,-1):
        if graph[i][y] == color:
            x_cnt += 1
        else:
            break
    for i in range(y+1,n):
        if graph[x][i] == color:
            y_cnt += 1
        else:
            break
    for i in range(y-1,-1,-1):
        if graph[x][i] == color:
            y_cnt += 1
        else:
            break

    return max(x_cnt,y_cnt)

n = int(input())

graph = []

for i in range(n):
    s = input()
    temp = []

    for j in s:
        temp.append(j)
    graph.append(temp)

max_cnt = 1

for i in range(n):
    for j in range(n):
        max_cnt = max(max_cnt, find(i,j))

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[i][j] == graph[nx][ny]:
                continue

            graph[i][j], graph[nx][ny] = graph[nx][ny], graph[i][j]
            max_cnt = max(max_cnt,find(i,j))
            max_cnt = max(max_cnt,find(nx,ny))
            graph[i][j], graph[nx][ny] = graph[nx][ny], graph[i][j]

print(max_cnt)