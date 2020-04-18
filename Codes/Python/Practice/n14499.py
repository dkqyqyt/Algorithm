N,M,x,y,K = map(int,input().split())

graph = []

dx = [0,0,-1,1]
dy = [1,-1,0,0]
dice = [[0 for _ in range(3)] for _ in range(4)]

for _ in range(N):
    graph.append(list(map(int,input().split())))

move = list(map(int,input().split()))

def move_west():
    global dice
    four = dice[1].pop(0)
    dice[1].append(dice[3][1])
    dice[3][1] = four

def move_east():
    global dice
    three = dice[1].pop()
    dice[1].insert(0,dice[3][1])
    dice[3][1] = three

def move_north():
    global dice
    for i in range(3):
        dice[i][1], dice[i+1][1] = dice[i+1][1], dice[i][1]

def move_south():
    global dice
    for i in range(2,-1,-1):
        dice[i][1], dice[i+1][1] = dice[i+1][1], dice[i][1]

for i in range(len(move)):
    # for row in dice:
    #     print(*row)
    # print()
    dir = move[i]

    next_x = x + dx[dir-1]
    next_y = y + dy[dir-1]

    if next_x >= N or next_x < 0 or next_y >= M or next_y < 0:
        continue
    if dir == 1:
        move_east()
    elif dir == 2:
        move_west()
    elif dir == 3:
        move_north()
    else:
        move_south()
    x = next_x
    y = next_y
    if graph[x][y] == 0:
        graph[x][y] = dice[3][1]
    else:
        dice[3][1] = graph[x][y]
        graph[x][y] = 0
    print(dice[1][1])