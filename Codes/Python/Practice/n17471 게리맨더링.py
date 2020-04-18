from collections import deque

N = int(input())
min_pop = 987654321
def track(depth, sector):
    global min_pop
    if depth == N:
        visit = [0]*(N+1)
        cnt = 0
        for i in range(1,N+1):
            if visit[i]:
                continue
            cnt += 1
            visit = bfs(i,visit,sector)

        if cnt != 2:
            return

        if isPossible(visit):
            one = 0
            two = 0
            for i in range(1,N+1):
                if sector[i] == 0:
                    one += population[i]
                else:
                    two += population[i]

            ans = abs(one-two)
            if ans < min_pop:
                min_pop = ans
        return
    sector.append(0)
    track(depth+1,sector)
    sector.pop()
    sector.append(1)
    track(depth+1,sector)
    sector.pop()

def bfs(node,visit,sector):
    que = deque()
    que.append(node)
    visit[node] = 1

    while que:
        now_node = que.popleft()

        for i in range(len(nodes[now_node])):
            if visit[nodes[now_node][i]]:
                continue
            if sector[nodes[now_node][i]] != sector[now_node]:
                continue
            que.append(nodes[now_node][i])
            visit[nodes[now_node][i]] = 1
    return visit

def isPossible(visit):
    for i in range(1,len(visit)):
        if not visit[i]:
            return False
    return True

population = list(map(int,input().split()))
population.insert(0,0)

nodes = [[] for _ in range(N+1)]

for i in range(1,N+1):
    info = list(map(int,input().split()))
    for j in range(1,len(info)):
        nodes[i].append(info[j])

track(0,[0])

if min_pop == 987654321:
    print(-1)
else:
    print(min_pop)