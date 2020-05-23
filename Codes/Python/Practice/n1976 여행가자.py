n = int(input())
len_route = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

routes = list(map(int,input().split()))
parents = [-1]*n

def find(node):
    if parents[node] == -1:
        return node
    parents[node] = find(parents[node])
    return parents[node]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return True

    if x > y:
        parents[x] = y
    else:
        parents[y] = x
    return False
for i in range(len(graph)):
    for j in range(i):
        if graph[i][j] == 1:
            union(i,j)

ans = 'YES'
for i in range(len(routes)):
    for j in range(i+1, len(routes)):
        if not union(routes[i]-1,routes[j]-1):
            ans = 'NO'
            break

print(ans)