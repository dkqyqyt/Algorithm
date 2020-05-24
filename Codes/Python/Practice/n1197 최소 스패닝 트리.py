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

v, e = map(int,input().split())

edges = [list(map(int,input().split())) for _ in range(e)]
parents = [-1]*(v+1)
edges.sort(key = lambda x:x[2])

w = 0
for edge in edges:
    if not union(edge[0], edge[1]):
        w += edge[2]

print(w)