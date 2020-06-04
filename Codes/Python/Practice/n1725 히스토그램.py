# [s,e) 구간
def histogram(s,e):
    if(s == e): return 0
    if(s+1 == e): return rec[s]

    mid = (s+e)//2
    result = max(histogram(s,mid), histogram(mid,e))

    w = 1
    h = rec[mid]
    l = mid
    r = mid
    while r-l+1 < e-s:
        if l - 1 >= s:
            p = min(h,rec[l-1])
        else:
            p = -1
        if r + 1 < e:
            q = min(h,rec[r+1])
        else:
            q = -1

        if p >= q:
            h = p
            l -= 1
        else:
            h = q
            r += 1

        result = max(result,(w+1)*h)
        w += 1

    return result

n = int(input())

rec = [int(input()) for _ in range(n)]

print(histogram(0,n))