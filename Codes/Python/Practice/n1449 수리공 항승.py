n, l = map(int,input().split())

line = [0 for _ in range(1001)]

repair = list(map(int,input().split()))
repair.sort()
cnt = 0
for i in range(len(repair)):
    if line[repair[i]]:
        continue
    cnt += 1
    for j in range(repair[i],repair[i]+l):
        if j >= 1001:
            break
        line[j] = 1

print(cnt)