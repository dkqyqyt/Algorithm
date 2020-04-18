N = int(input())
ans = 987654321
materials = []

for _ in range(N):
    materials.append(list(map(int,input().split())))

def track(depth, sin, sseun, pre_idx,path):
    global ans
    now_taste = abs(sin-sseun)
    if depth!= 0 and now_taste < ans:
        print(now_taste)
        print(*path)
        ans = now_taste
    if depth == N:
        return

    for i in range(pre_idx+1,N):
        path.append(materials[i])
        track(depth+1, sin*materials[i][0], sseun+materials[i][1], i,path)
        path.pop()

track(0,1,0,-1,[])
print(ans)