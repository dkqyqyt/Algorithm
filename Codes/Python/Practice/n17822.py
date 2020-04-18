dx = [1,-1,0,0]
dy = [0,0,1,-1]

N,M,T = map(int,input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

def link(index,length):
    if index == -1:
        return length-1
    elif index == length:
        return 0

def notchanged(graph):
    total = 0
    cnt = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                continue
            total += graph[i][j]
            cnt += 1
    if cnt == 0:
        return graph
    aver = total/cnt
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                continue
            if graph[i][j] > aver:
                graph[i][j] -= 1
            elif graph[i][j] < aver:
                graph[i][j] += 1
    return graph

def myRemove(graph,x,y):
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if next_x >= len(graph) or next_x < 0:
            continue
        if next_y >= len(graph[0]) or next_y < 0:
            next_y = link(next_y, len(graph[0]))
        if graph[next_x][next_y] == graph[x][y]:
            return True
    return False

def makeGraph(graph):
    new_graph = [[0 for _ in range(M)] for _ in range(N)]
    check = False
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                continue
            if myRemove(graph,i,j):
                check = True
                new_graph[i][j] = 0
            else:
                new_graph[i][j] = graph[i][j]

    if not check:
        new_graph = notchanged(new_graph)

    return new_graph

def turn(graph,d,i):
    tmp = []
    if d == 0:
        tmp.append(graph[i][-1])
        tmp.extend(graph[i][:-1])
    else:
        tmp.extend(graph[i][1:])
        tmp.append(graph[i][0])
    graph[i] = tmp

for _ in range(T):
    x,d,k = map(int,input().split())
    for i in range(len(graph)):
        if (i+1)%x == 0:
            for _ in range(k):
                turn(graph,d,i)
    # for row in graph:
    #     print(*row)
    # print('---')
    graph = makeGraph(graph)
    # for row in graph:
    #     print(*row)
    # print()
ans = 0
for row in graph:
    ans += sum(row)

print(ans)