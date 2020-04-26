from collections import deque

start, end = map(int,input().split())

visit = [987654321 for _ in range(200001)]

def bfs(start):
    que = deque()
    time = 0
    que.append((start,time))
    visit[start] = time

    while que:
        next_p, t = que.popleft()

        if next_p - 1 >= 0:
            if visit[next_p - 1] > t + 1:
                que.append((next_p-1,t+1))
                visit[next_p - 1] = t+1

        if next_p + 1 < 200001:
            if visit[next_p + 1] > t + 1:
                que.append((next_p+1,t+1))
                visit[next_p + 1] = t+1

        if next_p * 2 < 200001:
            if visit[next_p * 2] > t:
                que.append((next_p*2,t))
                visit[next_p*2] = t

bfs(start)
print(visit[end])
