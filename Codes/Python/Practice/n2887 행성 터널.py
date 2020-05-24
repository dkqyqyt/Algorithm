def find(node):
    if parents[node] < 0:
        return node
    parents[node] = find(parents[node])
    return parents[node]

def union(x,y):
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
points = []
edges = []
parents = [-1]*n

for i in range(n):
    x,y,z = list(map(int,input().split()))
    points.append([x,y,z,i])

for i in range(3):
    points.sort(key = lambda x:x[i])
    b_loc = points[0][3]
    for j in range(n-1):
        next_loc = points[j+1][3]
        edges.append([abs(points[j+1][i] - points[j][i]), b_loc,next_loc])
        b_loc = next_loc

edges.sort(key = lambda x:x[0])

weight = 0
num_of_edge = 0

for edge in edges:
    if num_of_edge == n-1:
        break
    if not union(edge[1], edge[2]):
        weight += edge[0]
        num_of_edge += 1
print(weight)