from collections import deque

def bfs(x,y):
    que = deque()
    visit = [[0 for _ in range(c)] for _ in range(r)]
    que.append((x,y))
    visit[x][y] = 1



TCs = int(input())

for tc in range(TCs):
    r,c = map(int,input().split())

    graph = []

    prisoner_loc = []
    graph.append(['.' for _ in range(c+2)])
    for i in range(r):
        s = input()
        tmp = ['.']
        for j in range(c):
            if s[j] == '$':
                prisoner_loc.append((i,j))
            tmp.append(s[j])
        tmp.append('.')
        graph.append(tmp)
    graph.append(['.' for _ in range(c+2)])

    bfs(0,0)
    bfs(prisoner_loc[0][0], prisoner_loc[0][1])
    bfs(prisoner_loc[1][0], prisoner_loc[1][1])