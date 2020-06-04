def find_arr(s,e):
    if s == e:
        return 0
    if s + 1 == e:
        return graph[s]**2

    mid = (s+e)//2
    result = max(find_arr(s,mid), find_arr(mid,e),graph[mid]**2)

    min_num = graph[mid]
    mysum = graph[mid]
    l = mid
    r = mid

    while r-l+1 < e-s:
        if l-1 >= s:
            p = min(min_num,graph[l-1])
        else:
            p = 0
        if r+1 < e:
            q = min(min_num, graph[r+1])
        else:
            q = 0

        if p >= q:
            min_num = p
            mysum += graph[l-1]
            result = max(result, mysum*min_num)
            l -= 1
        else:
            min_num = q
            mysum += graph[r+1]
            result = max(result, mysum*min_num)
            r += 1

    return result

n = int(input())

graph = list(map(int,input().split()))

print(find_arr(0,n))