def track(depth, path):
    if depth == M:
        print(*path)
        return

    for num in nums:
        if num in path:
            continue
        path.append(num)
        track(depth+1,path)
        path.pop()

N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

track(0,[])
