def dfs(node, dist):
    global max_dist, next_root
    flag = False
    for i in range(len(nodes[node])):
        if visit[nodes[node][i][0]]:
            continue
        flag = True
        visit[nodes[node][i][0]] = 1
        dfs(nodes[node][i][0], dist + nodes[node][i][1])
        visit[nodes[node][i][0]] = 0
    if not flag:
        if dist > max_dist:
            max_dist = dist
            next_root = node

n = int(input())
nodes = [[] for _ in range(10001)]

for _ in range(n-1):
    parent, child, weight = map(int,input().split())
    nodes[parent].append((child,weight))
    nodes[child].append((parent,weight))

max_dist = 0
next_root = None

visit = [0 for _ in range(10001)]
visit[1] = 1
dfs(1,0)
max_dist = 0
visit = [0 for _ in range(10001)]
dfs(next_root,0)
print(max_dist)

