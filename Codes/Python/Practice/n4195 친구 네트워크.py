def find(node):
    if parents[node] < 0:
        return node
    parents[node] = find(parents[node])
    return parents[node]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return -parents[x]

    if x > y:
        parents[y] += parents[x]
        parents[x] = y
        return -parents[y]
    else:
        parents[x] += parents[y]
        parents[y] = x
        return -parents[x]

TCs = int(input())

for tc in range(TCs):
    f = int(input())
    parents = [-1]*100001
    index = 0
    dict = {}
    for i in range(f):
        p_list = input().split()
        if p_list[0] in dict.keys():
            i1 = dict[p_list[0]]
        else:
            dict[p_list[0]] = index
            i1 = index
            index += 1

        if p_list[1] in dict.keys():
            i2 = dict[p_list[1]]
        else:
            dict[p_list[1]] = index
            i2 = index
            index += 1
        print(union(i1,i2))