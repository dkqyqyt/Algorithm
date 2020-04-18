import sys

R,C,M = map(int,input().split())
if M == 0:
    print(0)
    sys.exit(0)
sharks = []

# r,c = 상어의 위치, s = 속력, d = 이동방향(1= 위, 2 = 아래, 3 = 오른쪽, 4 = 왼쪽), z = 크기
graph = [[[] for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    if d == 3 or d == 4:
        s = s%((C-1)*2)
    else:
        s = s%((R-1)*2)
    graph[r-1][c-1] = [z,d,s]

def move(r,c,z,d,s):
    movement = 0
    if d == 1:
        plus = False
        while movement < s:
            if plus:
                r += 1
                if r > R-1:
                    plus = False
                    r -= 2
                movement += 1
            else:
                r -= 1
                if r < 0:
                    plus = True
                    r += 2
                movement += 1
        if plus:
            d = 2
        else:
            d = 1
    elif d == 2:
        plus = True
        while movement < s:
            if plus:
                r += 1
                if r > R-1:
                    plus = False
                    r -= 2
                movement += 1

            else:
                r -= 1
                if r < 0:
                    plus = True
                    r += 2
                movement += 1
        if plus:
            d = 2
        else:
            d = 1
    elif d == 3:
        plus = True
        while movement < s:
            if plus:
                c += 1
                if c > C-1:
                    plus = False
                    c -= 2
                movement += 1

            else:
                c -= 1
                if c < 0:
                    plus = True
                    c += 2
                movement += 1

        if plus:
            d = 3
        else:
            d = 4
    else:
        plus = False
        while movement < s:
            if plus:
                c += 1
                if c > C-1:
                    plus = False
                    c -= 2
                movement += 1

            else:
                c -= 1
                if c < 0:
                    plus = True
                    c += 2
                movement += 1

        if plus:
            d = 3
        else:
            d = 4
    if not new_graph[r][c]:
        new_graph[r][c] = [z, d, s]
    elif new_graph[r][c][0] < z:
        new_graph[r][c] = [z, d, s]

loc = -1
ans = 0
for time in range(C):
    loc += 1
    for r in range(R):
        if not graph[r][loc]:
            continue
        ans += graph[r][loc][0]
        graph[r][loc] = []
        break

    new_graph = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if not graph[i][j]:
                continue
            move(i,j,graph[i][j][0],graph[i][j][1],graph[i][j][2])
    graph = new_graph

# for i in range(R):
#     for j in range(C):
#         print(graph[i][j], end = ' ')
#     print()

print(ans)