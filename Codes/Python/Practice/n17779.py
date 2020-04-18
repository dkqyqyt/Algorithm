# 1 < x <= N-2
# 1+d1 <= y <= N-d2 || 2 <= y <= N-1
# d1 + d2 <= N - x
# 1 <= d1 <= y - 1
# 1 <= d2 <= N - y

N = int(input())

people = []

for _ in range(N):
    people.append(list(map(int,input().split())))

ans = 987654321

for x in range(N):
    for y in range(N):
        for d1 in range(1,N):
            for d2 in range(1,N):
                if x+d1+d2 > N-1:
                    continue
                if y+d2 > N-1:
                    continue
                if x < 0:
                    continue
                if y-d1 < 0:
                    continue

                sector = [[0 for _ in range(N)] for _ in range(N)]
                p = [0,0]
                for i in range(d2+1):
                    for j in range(d1+1):
                        sector[x+p[0]+j][y+p[0]-j] = 5
                    p[0] += 1
                    p[1] += 1
                for i in range(len(sector)):
                    minn = -1
                    maxn = -1
                    for j in range(len(sector[i])):
                        if sector[i][j] == 5:
                            if minn == -1:
                                minn = j
                                continue
                            maxn = j
                    # print(minn,maxn)
                    if maxn != -1:
                        for k in range(minn,maxn):
                            sector[i][k] = 5

                for i in range(0,x+d1):
                    for j in range(0,y+1):
                        if sector[i][j] != 5:
                            sector[i][j] = 1
                        else:
                            break
                for i in range(0,x+d2+1):
                    for j in range(N-1,y,-1):
                        if sector[i][j] != 5:
                            sector[i][j] = 2
                        else:
                            break
                for i in range(x+d1,N):
                    for j in range(y-d1+d2):
                        if sector[i][j] != 5:
                            sector[i][j] = 3
                        else:
                            break
                for i in range(x+d2+1,N):
                    for j in range(N-1,y-d1+d2-1,-1):
                        if sector[i][j] != 5:
                            sector[i][j] = 4
                        else:
                            break

                # print(x,y,d1,d2)
                # for row in sector:
                #     print(*row)
                # print('---')
                pe = [0,0,0,0,0]
                for i in range(N):
                    for j in range(N):
                        pe[sector[i][j]-1] += people[i][j]
                # print(pe)
                if max(pe)-min(pe) < ans:
                    ans = max(pe) - min(pe)
                    # print(ans)
                    # print(pe)
                    # for row in sector:
                    #     print(*row)
                    # print('---')
print(ans)