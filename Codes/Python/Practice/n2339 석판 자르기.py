def jew_num(rs,re,cs,ce):
    cnt = 0
    for i in range(rs,re):
        for j in range(cs,ce):
            if graph[i][j] == 2:
                cnt += 1
    return cnt

def impurity_num(rs,re,cs,ce):
    impure_loc = []
    for i in range(rs, re):
        for j in range(cs, ce):
            if graph[i][j] == 1:
                impure_loc.append((i,j))
    return impure_loc

def rock(rs,re,cs,ce,dir):
    global ans
    jew = jew_num(rs,re,cs,ce)
    impure_loc = impurity_num(rs,re,cs,ce)
    if re <= 0 or rs >= n or ce <= 0 or cs >= n:
        return 1
    if jew == 0:
        return 0
    if jew == 1:
        if len(impure_loc)==0:
            return 1
        else:
            return 0
    if len(impure_loc) == 0:
        return 0
    result = 0
    # print(impure_loc)
    for x,y in impure_loc:
        if dir != 1: # 세로로 자름
            flag = False
            for i in range(rs,re):
                if graph[i][y] == 2:
                    flag = True
                    break
            if not flag:
                result += rock(rs,re,cs,y,1) * rock(rs,re,y+1,ce,1)
        if dir != 0:
            flag = False
            for i in range(cs, ce):
                if graph[x][i] == 2:
                    flag = True
                    break
            if not flag:
                result += rock(rs,x,cs,ce,0) * rock(x+1,re,cs,ce,0)

    return result

n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

ans = rock(0,n,0,n,-1)
if ans == 0:
    print(-1)
else:
    print(ans)