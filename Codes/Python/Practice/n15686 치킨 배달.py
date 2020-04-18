N, M = map(int,input().split())

graph = []
homes = []
total_chickens = []
dists = []
chickens = []

for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 1:
            homes.append((i,j))
        elif tmp[j] == 2:
            total_chickens.append((i,j))
    graph.append(tmp)

def track(depth,path,idx):
    if depth == M:
        tmp = []
        for item in path:
            tmp.append(item)
        chickens.append(tmp)
        return

    for i in range(idx+1,len(total_chickens)):
        path.append(total_chickens[i])
        track(depth+1, path, i)
        path.pop()

track(0,[],-1)
# print(total_chickens)
# print(chickens)
min_dist = 987654321
for chicken in chickens:
    dists = [987654321]*len(homes)
    for ch_loc in chicken:
        for i in range(len(homes)):
            dist = abs(ch_loc[0] - homes[i][0]) + abs(ch_loc[1] - homes[i][1])
            if dists[i] > dist:
                dists[i] = dist
    s = sum(dists)
    if min_dist > s:
        min_dist = s

print(min_dist)