def check(x,y):
    cnt = 0
    color = graph[x][y]
    for i in range(8):
        for j in range(8):
            if color == 'W':
                if chess_W[i][j] != graph[x+i][y+j]:
                    cnt += 1
            else:
                if chess_B[i][j] != graph[x+i][y+j]:
                    cnt += 1
    return cnt

r,c = map(int,input().split())
graph = []

for i in range(r):
    s = input()
    temp = []
    for j in range(c):
        temp.append(s[j])
    graph.append(temp)

chess_W = [[0]*8 for _ in range(8)]
chess_B = [[0]*8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            chess_W[i][j] = 'W'
            chess_B[i][j] = 'B'
        else:
            chess_W[i][j] = 'B'
            chess_B[i][j] = 'W'

min_cnt = 987654321
for i in range(r-7):
    for j in range(c-7):
        change = check(i,j)
        min_cnt = min(min_cnt,change,64-change)

print(min_cnt)
