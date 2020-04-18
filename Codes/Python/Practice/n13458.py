N = int(input())

classes = []


classes = list(map(int,input().split()))

B,C = map(int,input().split())

ans = 0

for i in range(N):
    if classes[i] <= B:
        ans += 1
        continue
    elif (classes[i]-B)%C == 0:
        ans += (classes[i]-B)//C +1
        continue
    ans += (classes[i] - B)//C + 2

print(ans)