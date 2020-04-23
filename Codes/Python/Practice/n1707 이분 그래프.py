from collections import deque

def bfs(start):
    que = deque()
    color = 0
    que.append(start)
    visit[start] = color

    while que:
        color = (color+1)%2
        for _ in range(len(que)):
            node = que.popleft()

            for i in range(len(graph[node])):
                next_node = graph[node][i]
                if visit[next_node] != -1:
                    if visit[next_node] == visit[node]:
                        # print(node,next_node)
                        return False
                    continue
                que.append(next_node)
                visit[next_node] = color
    return True

TCs = int(input())

for tc in range(TCs):
    v,e = map(int,input().split())
    answer = None

    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        node1, node2 = map(int,input().split())

        graph[node1].append(node2)
        graph[node2].append(node1)

    visit = [-1 for _ in range(v+1)]
    for i in range(1,len(graph)):
        if answer == False:
            continue
        if visit[i] == -1:
            answer = bfs(i)
    # print(visit)
    # print(answer)
    if answer:
        print('YES')
    else:
        print('NO')