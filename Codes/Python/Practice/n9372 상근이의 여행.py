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

TCs = int(input())

for tc in range(TCs):
    n, m = map(int,input().split())

    parents = [-1]*(n+1)

    cnt = 0
    for i in range(m):
        a,b = map(int,input().split())

        if not union(a,b):
            cnt += 1
    print(cnt)

