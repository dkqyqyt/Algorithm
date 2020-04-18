import sys

graph = []

loc = []
for i in range(10):
    tmp = list(map(int,input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 1:
            loc.append((i,j))
    graph.append(tmp)

if len(loc) == 0:
    print(0)
    sys.exit(0)
visit = [[0 for _ in range(10)] for _ in range(10)]
paper = [5]*5
min_use = 987654321
def canMake(x,y,wide):
    if x+wide-1 >= 10 or y+wide-1 >=10:
        return False
    for i in range(wide):
        for j in range(wide):
            if graph[x+i][y+j] == 0:
                return False
            if visit[x+i][y+j]:
                return False
    return True

def track(use,idx):
    global min_use

    if use >= min_use:
        return
    if idx == len(loc):
        if use < min_use:
            min_use = use
        return

    x = loc[idx][0]
    y = loc[idx][1]
    if visit[x][y]:
        track(use,idx+1)
    else:
        for w in range(5,1,-1):
            if paper[w-1] <= 0:
                continue
            if canMake(x,y,w):
                for i in range(w):
                    for j in range(w):
                        visit[x+i][y+j] = 1
                paper[w-1] -= 1
                track(use+1,idx+1)
                for i in range(w):
                    for j in range(w):
                        visit[x+i][y+j] = 0
                paper[w-1] += 1

        if paper[0] > 0:
            visit[x][y] = 1
            paper[0] -= 1
            track(use+1,idx+1)
            visit[x][y] = 0
            paper[0] += 1

track(0,0)

if min_use == 987654321:
    print(-1)
else:
    print(min_use)