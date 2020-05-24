import math

def find(node):
    if parents[node] < 0:
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

n, m = map(int,input().split())

points = [list(map(int,input().split())) for _ in range(n)]
parents = [-1]*(n+1)
edges = []

for i in range(len(points)):
    for j in range(i+1,len(points)):
        d_x = abs(points[i][0] - points[j][0])
        d_y = abs(points[i][1] - points[j][1])
        edges.append([i,j,math.sqrt(math.pow(d_x,2)+math.pow(d_y,2))])
edges.sort(key = lambda x:x[2])

for i in range(m):
    a,b = map(int,input().split())
    union(a-1,b-1)
weight = 0
for edge in edges:
    if not union(edge[0], edge[1]):
        weight += edge[2]

print('%.2f'%weight)


