def chdir(preMove, dir):
    if preMove == (1,0):
        if dir == 'L':
            return (0,1)
        else:
            return (0,-1)
    elif preMove == (0,1):
        if dir == 'L':
            return (-1,0)
        else:
            return (1,0)
    elif preMove == (0,-1):
        if dir == 'L':
            return (1,0)
        else:
            return (-1,0)
    else:
        if dir == 'L':
            return (0,-1)
        else:
            return (0,1)

lenOfmap = int(input())
numOfapple = int(input())
graph = [[0 for _ in range(lenOfmap)] for _ in range(lenOfmap)]

for _ in range(numOfapple):
    x,y = map(int,input().split())
    graph[x][y] = 1

numOfdir = int(input())

dirs = []

for _ in range(numOfdir):
    tmp = input().split()
    tmp[0] = int(tmp[0])
    dirs.append(tmp)
x = y = 0
tail_x = 0
tail_y = 0
graph[x][y] = 2
move = (1,0)
tail_move = (1,0)
tail_time = []
time = 0
sizes = 1
while True:
    # for row in graph:
    #     print(*row)
    # print()
    x = x + move[0]
    y = y + move[1]

    time += 1
    if x >= lenOfmap or x < 0 or y >= lenOfmap or y < 0:
        break
    if graph[x][y] == 2:
        break

    if graph[x][y] != 1:
        graph[x][y] = 2
        graph[tail_x][tail_y] = 0
        tail_x = tail_x+tail_move[0]
        tail_y = tail_y+tail_move[1]
    else:
        sizes += 1
        graph[x][y] = 2

    if time == dirs[0][0]:
        tail_time.append((sizes-1,(move[0],move[1]),dirs[0][1]))
        move = chdir(move,dirs[0][1])
        dirs.pop(0)

    if len(tail_time) != 0:
        if tail_time[0][0] == time:
            tail_move = chdir(tail_time[0][1],tail_time[0][2])
            tail_time.pop(0)

print(time)
