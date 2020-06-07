import heapq

n = int(input())


infos = []
for i in range(n):
    infos.append(list(map(int,input().split())))
infos.sort()
que = []

heapq.heappush(que,infos[0][1])

for i in range(1,len(infos)):
    s,e = infos[i]
    first_time = heapq.heappop(que)
    if first_time <= s:
        heapq.heappush(que,e)
    else:
        heapq.heappush(que,first_time)
        heapq.heappush(que,e)

print(len(que))