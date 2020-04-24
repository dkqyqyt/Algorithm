from collections import deque

S = int(input())

def bfs(length, clipboard):
    que = deque()
    que.append((length, clipboard))
    visit = [[0 for _ in range(2001)] for _ in range(2001)]
    time = 0

    while que:
        for _ in range(len(que)):
            now_len, now_clip = que.popleft()
            if now_len > 2000 or now_clip > 2000:
                continue
            # print(now_len, now_clip)
            if now_len == S:
                return time
            if not visit[now_len][now_len]:
                que.append((now_len, now_len))
                visit[now_len][now_len] = 1

            if not now_len + now_clip > 2000:
                if not visit[now_len+now_clip][now_clip]:
                    if now_clip != 0:
                        que.append((now_len + now_clip, now_clip))
                        visit[now_len + now_clip][now_clip] = 1
            if now_len > 2:
                if not visit[now_len-1][now_clip]:
                    que.append((now_len-1, now_clip))
                    visit[now_len - 1][now_clip] = 1
        time += 1

print(bfs(1,0))