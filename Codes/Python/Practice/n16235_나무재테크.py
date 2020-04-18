n,m,K = map(int,input().split())

dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,1,1,-1,-1]
A = []
trees = [[[] for _ in range(n)] for _ in range(n)]
dead_trees = [[[] for _ in range(n)] for _ in range(n)]
foods = [[5 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    A.append(list(map(int,input().split())))

for _ in range(m):
    r,c,size = map(int,input().split())
    trees[r-1][c-1].append(size)

def spring():
    global trees
    global dead_trees
    global foods
    for i in range(n):
        for j in range(n):
            if not trees[i][j]:
               continue
            flag = len(trees[i][j])
            for k in range(len(trees[i][j])):
                if trees[i][j][k] <= foods[i][j]:
                    foods[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    flag = k
                    break
            end = len(trees[i][j])
            for _ in range(flag,end):
                dead_trees[i][j].append(trees[i][j].pop())

def summer():
    global foods
    global dead_trees
    for i in range(n):
        for j in range(n):
            if not dead_trees[i][j]:
                continue
            for k in range(len(dead_trees[i][j])):
                foods[i][j] += dead_trees[i][j][k]//2
            dead_trees[i][j].clear()

def autumn():
    global trees
    for i in range(n):
        for j in range(n):
            if not trees[i][j]:
                continue
            for k in range(len(trees[i][j])):
                if trees[i][j][k]%5 != 0:
                    continue
                for l in range(8):
                    next_x = i+dx[l]
                    next_y = j+dy[l]

                    if next_x >= n or next_x < 0 or next_y >= n or next_y < 0:
                        continue
                    trees[next_x][next_y].insert(0,1)

def winter():
    global A
    global foods
    for i in range(n):
        for j in range(n):
            foods[i][j] += A[i][j]

def findtrees():
    global trees
    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += len(trees[i][j])
    return cnt

for _ in range(K):
    spring()
    summer()
    autumn()
    winter()

print(findtrees())
