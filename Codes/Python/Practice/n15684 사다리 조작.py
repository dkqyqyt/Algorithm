import sys

N, M, H = map(int,input().split())
# N : 세로선의 개수, M : 가로선의 개수, H : 세로선마다 가로선을 놓을 수 있는 위치의 개
if M == 0:
    print(0)
    sys.exit(0)

graph = [[0 for _ in range(N-1)] for _ in range(H)]

for i in range(M):
    x,y = map(int,input().split())
    graph[x-1][y-1] = 1

def check():
    for idx in range(N):
        first_idx = idx
        for j in range(H):
            if move_left(idx,j):
                idx -= 1
                continue
            if idx != N-1:
                if move_right(idx,j):
                    idx += 1
                    continue
        if first_idx != idx:
            return False
    return True

def move_left(idx, height):
    if idx-1 < 0:
        return False
    left_bridge = graph[height][idx-1]
    if left_bridge:
        return True
    return False

def move_right(idx, height):
    if idx > N-2:
        return False
    right_bridge = graph[height][idx]
    if right_bridge:
        return True
    return False

candidates = []
def track(depth, x,y, candi):
    global min_ans
    if depth > min_ans:
        return
    if check():
        if depth < min_ans:
            min_ans = depth
    if depth == 3:
        return

    for i in range(y, N-1):
        for j in range(H):
            if graph[j][i] == 1:
                continue
            left = i - 1
            right = i + 1
            if left >= 0:
                if graph[j][left] == 1:
                    continue
            if right < N - 1:
                if graph[j][right] == 1:
                    continue
            graph[j][i] = 1
            candi.append((j,i))
            track(depth+1,j,i,candi)
            candi.pop()
            graph[j][i] = 0

min_ans = 987654321
track(0,0,0,[])

if min_ans == 987654321:
    print(-1)
else:
    print(min_ans)

