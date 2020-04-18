def trans(arr):
    x = len(arr)
    y = len(arr[0])
    result = [[0 for _ in range(x)] for _ in range(y)]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            result[j][i] = arr[i][j]
    return result

def mySort(arr, byrow):
    if not byrow:
        arr = trans(arr)
    result = []
    maxlen = 0
    for row in arr:
        maxn = max(row)
        tmp = [0 for i in range(maxn+1)]
        for num in row:
            if num == 0:
                continue
            tmp[num] += 1

        ll = []
        for i in range(len(tmp)):
            if tmp[i] == 0:
                continue
            ll.append((tmp[i],i))
        ll.sort()
        l = []
        for i in range(len(ll)):
            l.extend([ll[i][1], ll[i][0]])
        if len(l) > 100:
            l = l[:100]
        if len(l) > maxlen:
            maxlen = len(l)
        result.append(l)
    for row in result:
        if len(row) >= maxlen:
            continue
        for i in range(maxlen-len(row)):
            row.append(0)

    if not byrow:
        result = trans(result)
    return result

r,c,k = map(int,input().split())
r -= 1
c -= 1
graph = []
for i in range(3):
    graph.append(list(map(int,input().split())))

time = 0
while True:
    if time > 100:
        print(-1)
        exit(0)
    # for row in graph:
    #     print(*row)
    # print('---')
    if len(graph) > r and len(graph[r]) > c:
        if graph[r][c] == k:
            break

    if len(graph) >= len(graph[0]):
        graph = mySort(graph,1)
    else:
        graph = mySort(graph,0)
    time += 1
print(time)