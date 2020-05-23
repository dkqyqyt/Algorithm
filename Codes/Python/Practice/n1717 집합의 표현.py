def find(node):
    if parents[node] == -1:
        return node
    parents[node] = find(parents[node])
    return parents[node]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y: # 같은 집합
        return

    if x > y:
        parents[x] = y
    else:
        parents[y] = x

def is_same_union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return True
    else:
        return False

n, m = map(int,input().split())

parents = [-1]*(n+1)

for i in range(m):
    action, a, b = map(int,input().split())
    if action == 0:
        union(a,b)
    else:
        if is_same_union(a,b):
            print('YES')
        else:
            print('NO')