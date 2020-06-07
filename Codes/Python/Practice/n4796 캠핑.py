tc = 1
while True:
    l,p,v = map(int,input().split())
    if l == 0 and p == 0 and v == 0:
        break

    ans = 0
    day = 0
    while day < v:
        if day+p < v:
            ans += l
            day += p
        else:
            ans += min(v-day,l)
            day += p
    print('Case %d: %d'%(tc,ans))
    tc += 1