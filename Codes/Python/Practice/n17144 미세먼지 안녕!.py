import sys
sys.setrecursionlimit(10**6)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
up_dx = [-1,0,1,0]
up_dy = [0,1,0,-1]
down_dx = [1,0,-1,0]
down_dy = [0,1,0,-1]

R, C, T = map(int,input().split())

graph = []
refresh = []

for i in range(R):
    tmp = list(map(int,input().split()))
    for j in range(len(tmp)):
        if tmp[j] == -1:
            refresh.append((i,j))

    graph.append(tmp)

def mysum(m_graph):
    result = 0
    for i in range(len(m_graph)):
        for j in range(len(m_graph[i])):
            result += m_graph[i][j]
    return result

def dust_move(d_graph, depth):
    if depth == T:
        print(mysum(d_graph)+2)
        sys.exit(0)

    new_graph = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(len(d_graph)):
        for j in range(len(d_graph[i])):
            if d_graph[i][j] == 0 or d_graph[i][j] == -1:
                continue
            move = d_graph[i][j]//5
            if move == 0:
                new_graph[i][j] += d_graph[i][j]
                continue

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx >= R or nx < 0 or ny >= C or ny < 0:
                    continue
                if d_graph[nx][ny] == -1:
                    continue
                new_graph[nx][ny] += move
                d_graph[i][j] -= move
            new_graph[i][j] += d_graph[i][j]
    # print('---')
    # for row in new_graph:
    #     print(*row)
    # print()
    new_graph = fresh_up(new_graph,refresh[0])
    new_graph = fresh_down(new_graph,refresh[1])
    # for row in new_graph:
    #     print(*row)
    # print()
    dust_move(new_graph,depth+1)

def fresh_up(u_graph,up_idx):
    direction = 0
    sx = up_idx[0]
    sy = up_idx[1]

    while True:
        # print(sx, sy)
        nx = sx + up_dx[direction]
        ny = sy + up_dy[direction]

        if nx > up_idx[0] or nx < 0 or ny >= C or ny < 0:
            direction += 1
            continue
        if nx == up_idx[0] and ny == up_idx[1]:
            u_graph[sx][sy] = 0
            break
        u_graph[sx][sy] = u_graph[nx][ny]
        sx = nx
        sy = ny
    u_graph[up_idx[0]][up_idx[1]] = -1
    return u_graph

def fresh_down(do_graph,down_idx):
    direction = 0
    sx = down_idx[0]
    sy = down_idx[1]

    while True:
        # print(sx, sy)
        nx = sx + down_dx[direction]
        ny = sy + down_dy[direction]

        if nx >= R or nx < down_idx[0] or ny >= C or ny < 0:
            direction += 1
            continue
        if nx == down_idx[0] and ny == down_idx[1]:
            do_graph[sx][sy] = 0
            break
        do_graph[sx][sy] = do_graph[nx][ny]
        sx = nx
        sy = ny
    do_graph[down_idx[0]][down_idx[1]] = -1
    return do_graph

dust_move(graph,0)