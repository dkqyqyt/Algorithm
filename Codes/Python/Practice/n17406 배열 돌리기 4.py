dx = [0,1,0,-1]
dy = [1,0,-1,0]

N, M, K = map(int,input().split())

fir_graph = []

for _ in range(N):
    fir_graph.append(list(map(int,input().split())))

turns = []

for _ in range(K):
    tmp = list(map(int,input().split()))
    tmp[0] -= 1
    tmp[1] -= 1
    turns.append(tmp)

permute = []

def track(depth,per):
    global min_num
    if depth == K:
        tmp = []
        for i in range(len(per)):
            tmp.append(turns[per[i]])
        permute.append(tmp)
        return

    for i in range(K):
        if i in per:
            continue
        per.append(i)
        track(depth+1,per)
        per.pop()

def turn(r,c,s):
    for i in range(1,s+1):
        sx = r-i
        sy = c-i
        tmp = graph[sx][sy]
        sx += dx[0]
        sy += dy[0]
        tmp, graph[sx][sy] = graph[sx][sy],tmp
        direction = 0
        while True:
            if sx == r-i and sy == c-i:
                break
            nx = sx + dx[direction]
            ny = sy + dy[direction]

            if nx > r+i or nx < r-i or ny > c+i or ny < c-i:
                direction = (direction+1)%4
                continue
            tmp, graph[nx][ny] = graph[nx][ny], tmp
            sx = nx
            sy = ny

def calArray(graph):
    nums = []
    for i in range(N):
        nums.append(sum(graph[i]))
    return min(nums)

track(0,[])
min_num = 987654321
# print(permute)

for p in range(len(permute)):
    graph = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(len(fir_graph)):
        for j in range(len(fir_graph[i])):
            graph[i][j] = fir_graph[i][j]

    for loc in range(len(permute[p])):
        # print(permute[p][loc])
        r = permute[p][loc][0]
        c = permute[p][loc][1]
        s = permute[p][loc][2]
        turn(r,c,s)
    # print(calArray(graph))
    min_num = min(min_num,calArray(graph))


print(min_num)