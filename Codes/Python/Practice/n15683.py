import copy

dx = [1,-1,0,0]
dy = [0,0,1,-1]
movement = [[],[0,1,2,3],[[0,1],[2,3]],[[1,2],[0,2],[0,3],[1,3]],[[0,1,2],[0,1,3],[0,2,3],[1,2,3]],[[0,1,2,3]]]
# 1번 i = 0,1,2,3
# 2번 i = (0,1),(2,3)
# 3번 i = (2,3),(1,3),(1,4),(2,4)
# 4번 i = (1,2,3),(1,2,4),(1,3,4),(2,3,4)
# 5번 i = (1,2,3,4)

N, M = map(int,input().split())
minn = 987654321
def deadArea(graph):
    cnt = 0
    for row in graph:
        for num in row:
            if num == 0:
                cnt += 1
    return cnt

def camera(idx,graph):
    global minn
    if idx >= len(cameras):
        # for row in graph:
        #     print(*row)
        # print()
        area = deadArea(graph)
        if area < minn:
            minn = area
        return
    x, y = cameras[idx][0], cameras[idx][1]
    firstx = x
    firsty = y
    number = cameras[idx][2]
    if number == 1:
        for i in movement[number]:
            new_graph = copy.deepcopy(graph)
            x = firstx
            y = firsty
            while True:
                x = x+dx[i]
                y = y+dy[i]

                if x >= N or x < 0 or y >= M or y < 0:
                    break
                if graph[x][y] == 6:
                    break
                new_graph[x][y] = '#'
            camera(idx+1,new_graph)
    if number == 2:
        for i in movement[number]:
            new_graph = copy.deepcopy(graph)

            for j in i:
                x = firstx
                y = firsty
                while True:
                    x = x + dx[j]
                    y = y + dy[j]

                    if x >= N or x < 0 or y >= M or y < 0:
                        break
                    if graph[x][y] == 6:
                        break
                    new_graph[x][y] = '#'
            camera(idx + 1, new_graph)
    if number == 3:
        for i in movement[number]:
            new_graph = copy.deepcopy(graph)

            for j in i:
                x = firstx
                y = firsty
                while True:
                    x = x + dx[j]
                    y = y + dy[j]

                    if x >= N or x < 0 or y >= M or y < 0:
                        break
                    if graph[x][y] == 6:
                        break
                    new_graph[x][y] = '#'
            camera(idx + 1, new_graph)
    if number == 4:
        for i in movement[number]:
            new_graph = copy.deepcopy(graph)

            for j in i:
                x = firstx
                y = firsty
                while True:
                    x = x + dx[j]
                    y = y + dy[j]

                    if x >= N or x < 0 or y >= M or y < 0:
                        break
                    if graph[x][y] == 6:
                        break
                    new_graph[x][y] = '#'
            camera(idx + 1, new_graph)
    if number == 5:
        for i in movement[number]:
            new_graph = copy.deepcopy(graph)

            for j in i:
                x = firstx
                y = firsty
                while True:
                    x = x + dx[j]
                    y = y + dy[j]

                    if x >= N or x < 0 or y >= M or y < 0:
                        break
                    if graph[x][y] == 6:
                        break
                    new_graph[x][y] = '#'
            camera(idx + 1, new_graph)
graph = []
cameras = []
for i in range(N):
    graph.append(list(map(int,input().split())))
    for j in range(len(graph[i])):
        if 0 < graph[i][j] < 6:
            cameras.append([i,j,graph[i][j]])
# print(cameras)
camera(0,graph)
# print(len(cameras))
print(minn)