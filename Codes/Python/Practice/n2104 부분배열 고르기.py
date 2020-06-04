def find_arr(s,e):
    if s == e:
        return 0
    if s + 1 == e:
        return graph[s]

    mid = (s+e)//2
    result = max(find_arr(s,mid), find_arr(mid,e))

    min_num = graph[mid]
    mysum = graph[mid]
    l = mid
    r = mid
    mid_result = mysum*min_num

    while l > s:
        l -= 1
        if graph[l] < min_num:
            temp = min(graph[l],min_num) * (mysum+graph[l])
            if temp > mid_result:
                mysum += graph[l]
                min_num = min(graph[l],min_num)
                mid_result = mysum * min_num
            else:
                l += 1
                break
        else:
            mysum += graph[l]
            mid_result = mysum * min_num
    while r < e-1:
        r += 1
        if graph[r] < min_num:
            temp = min(graph[r],min_num) * (mysum+graph[r])
            if temp > mid_result:
                mysum += graph[r]
                min_num = min(graph[r],min_num)
                mid_result = mysum * min_num
            else:
                r -= 1
                break
        else:
            mysum += graph[r]
            mid_result = mysum * min_num

    # print('s,e : ', s, e)
    # print('l,r: ', l , r)
    # print('result: ', result)
    # print('mid_result: ', mid_result)

    return max(result, mid_result)
n = int(input())

graph = list(map(int,input().split()))

print(find_arr(0,n))