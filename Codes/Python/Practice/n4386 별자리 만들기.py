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

n = int(input())
stars = []
for i in range(n):
    x, y = map(float,input().split())
    stars.append((x,y))

edges = []
for i in range(len(stars)):
    for j in range(i+1,len(stars)):
        dist_x = abs(stars[i][0] - stars[j][0])
        dist_y = abs(stars[i][1] - stars[j][1])
        edges.append([i,j,round(math.sqrt(math.pow(dist_x,2) + math.pow(dist_y,2)), 2)])

edges.sort(key = lambda x:x[2])

parents = [-1]*(n+1)
weight = 0
for edge in edges:
    if not union(edge[0], edge[1]):
        weight += edge[2]

print(weight)