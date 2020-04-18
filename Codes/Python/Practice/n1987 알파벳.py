# import sys
# sys.setrecursionlimit(10**6)

R, C = map(int,input().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

graph= []

for i in range(R):
    s = input()
    tmp = []
    for char in s:
        tmp.append(char)
    graph.append(tmp)

alpha = [0]*26
max_dist = 0
def dfs(depth,point,alpha):
    global max_dist
    x = point[0]
    y = point[1]

    if depth > max_dist:
        max_dist = depth

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= R or nx < 0 or ny >= C or ny < 0:
            continue
        if alpha[ord(graph[nx][ny])-65]:
            continue
        alpha[ord(graph[nx][ny])-65] = 1
        dfs(depth+1,(nx,ny),alpha)
        alpha[ord(graph[nx][ny]) - 65] = 0


alpha[ord(graph[0][0])-65] = 1
dfs(1,(0,0),alpha)

print(max_dist)