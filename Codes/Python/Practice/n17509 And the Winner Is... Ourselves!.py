times = []

for i in range(11):# ddd
    info = list(map(int,input().split()))
    times.append(info)
times.sort()

time = 0
verdicts= 0
ans = 0
for i in range(len(times)):
    time += times[i][0]
    ans += time
    verdicts += times[i][1]

ans += verdicts*20
print(ans)