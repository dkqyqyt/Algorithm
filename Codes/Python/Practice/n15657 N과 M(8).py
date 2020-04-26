N, M = map(int,input().split())

nums = list(map(int,input().split()))
nums.sort()
def track(depth, path):
    if depth == M:
        print(*path)
        return

    for num in nums:
        if len(path):
            if path[-1] > num:
                continue
        path.append(num)
        track(depth+1, path)
        path.pop()

track(0,[])