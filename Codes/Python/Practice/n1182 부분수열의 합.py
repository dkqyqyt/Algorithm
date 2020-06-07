def track(depth, idx, mysum):
    global cnt
    if depth == n:
        if mysum == s:
            cnt += 1
        return
    track(depth+1,idx+1,mysum)
    track(depth+1,idx+1,mysum+nums[idx])

n,s = map(int,input().split())
nums = list(map(int,input().split()))
cnt = 0
track(0,0,0)
if s == 0:
    cnt -= 1
print(cnt)
