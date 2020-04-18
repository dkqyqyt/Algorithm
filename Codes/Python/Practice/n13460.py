import copy

N, M = map(int,input().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]
graph= None

ggraph = []
R = []
B = []
min = 987654321
for i in range(N):
    chars = input()
    tmp = []
    for j in range(len(chars)):
        if chars[j] == 'R':
            R = [i,j]
        elif chars[j] == 'B':
            B = [i,j]
        tmp.append(chars[j])
    ggraph.append(tmp)

# 0 = 위, 1 = 아래, 2 = 왼쪽, 3 = 오른쪽

def track(depth,path):
    global paths
    if depth >= 9:
        tmp = []
        for i in range(len(path)):
            tmp.append(path[i])
        paths.append(tmp)
        return

    for i in range(4):
        if path[-1] == i:
            continue
        path.append(i)
        track(depth+1,path)
        path.pop()

paths = []
for i in range(4):
    track(0,[i])

# for i in range(len(paths)):
#     print(paths[i])

bool = 0
# dir 1 : down, 2 : up, 3 : right, 4 : left

def moveR(dir, Rx, Ry):
    global bool
    graph[Rx][Ry] = '.'
    nextx = Rx + dx[dir]
    nexty = Ry + dy[dir]
    # print(nextx,nexty)
    if graph[nextx][nexty] == '#' or graph[nextx][nexty] =='B':
        # print(11)
        graph[Rx][Ry] = 'R'
        # for row in graph:
        #     print(*row)
        # print()
        return [Rx,Ry]
    elif graph[nextx][nexty] == 'O':
        if bool == 0:
            bool = 1
        return [Rx,Ry]
    else:
        return moveR(dir,nextx,nexty)
def moveB(dir, Bx, By):
    global bool
    graph[Bx][By] = '.'
    nextx = Bx + dx[dir]
    nexty = By + dy[dir]
    # for row in graph:
    #     print(*row)
    # print()
    if graph[nextx][nexty] == '#' or graph[nextx][nexty] == 'R':
        graph[Bx][By] = 'B'
        return [Bx,By]
    if graph[nextx][nexty] == 'O':
        bool = 2
        return [Bx,By]
    else:
        return moveB(dir,nextx,nexty)
def moveUp(R_dir,B_dir):
    x1, y1 = R_dir[0], R_dir[1]
    x2, y2 = B_dir[0], B_dir[1]

    if y1 == y2:
        if x1 > x2:
            B_dir = moveB(1,x2,y2)
            R_dir = moveR(1,x1,y1)
        else:
            R_dir = moveR(1,x1,y1)
            B_dir = moveB(1,x2,y2)
    else:
        R_dir = moveR(1,x1,y1)
        B_dir = moveB(1,x2,y2)
    return R_dir, B_dir

def moveDown(R_dir, B_dir):
    x1, y1 = R_dir[0], R_dir[1]
    x2, y2 = B_dir[0], B_dir[1]

    if y1 == y2:
        if x1 < x2:
            B_dir = moveB(0, x2, y2)
            R_dir = moveR(0, x1, y1)
        else:
            R_dir = moveR(0, x1, y1)
            B_dir = moveB(0, x2, y2)
    else:
        R_dir = moveR(0, x1, y1)
        B_dir = moveB(0, x2, y2)
    return R_dir, B_dir

def moveRight(R_dir, B_dir):
    x1, y1 = R_dir[0], R_dir[1]
    x2, y2 = B_dir[0], B_dir[1]

    if x1 == x2:
        if y1 < y2:
            B_dir = moveB(2, x2, y2)
            R_dir = moveR(2, x1, y1)
        else:
            R_dir = moveR(2, x1, y1)
            B_dir = moveB(2, x2, y2)
    else:
        R_dir = moveR(2, x1, y1)
        B_dir = moveB(2, x2, y2)
    return R_dir, B_dir

def moveLeft(R_dir, B_dir):
    x1, y1 = R_dir[0], R_dir[1]
    x2, y2 = B_dir[0], B_dir[1]

    if x1 == x2:
        if y1 > y2:
            B_dir = moveB(3, x2, y2)
            R_dir = moveR(3, x1, y1)
        else:
            R_dir = moveR(3, x1, y1)
            B_dir = moveB(3, x2, y2)
    else:
        R_dir = moveR(3, x1, y1)
        B_dir = moveB(3, x2, y2)

    return R_dir,B_dir

def move(RR,BB,path):
    global min
    global bool
    for i in range(len(path)):
        direction = path[i]
        if direction == 0:
            RR,BB = moveUp(RR,BB)
        elif direction == 1:
            RR,BB = moveRight(RR,BB)
        elif direction == 2:
            RR,BB = moveDown(RR,BB)
        else:
            RR,BB = moveLeft(RR,BB)
        # print(RR,BB)
        # for row in graph:
        #     print(*row)
        # print()
        if bool == 1:
            if min > i+1:
                min = i+1
            bool = 0
            return
        elif bool == 2:
            bool = 0
            return
RR = [R[0],R[1]]
BB = [B[0],B[1]]

for i in range(len(paths)):
    graph = []
    graph = copy.deepcopy(ggraph)
    RR = [R[0], R[1]]
    BB = [B[0], B[1]]
    # for row in graph:
    #     print(*row)

    move(R,B,paths[i])
if min > 10:
    print(-1)
else:
    print(min)