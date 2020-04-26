N = int(input())

ans = [[0 for _ in range(N)] for _ in range(N)]

def star(sx,sy,ex,ey):
    w = ex-sx
    if w == 3:
        for i in range(sx,ex):
            for j in range(sy,ey):
                if i == sx+1 and j == sy + 1:
                    continue
                ans[i][j] = '*'
        return

    w = w//3
    star(sx,sy,sx+w,sy+w)
    star(sx,sy+w,sx+w,sy+2*w)
    star(sx,sy+2*w,sx+w,sy+3*w)
    star(sx+w,sy,sx+2*w,sy+w)
    star(sx+w,sy+2*w,sx+2*w, sy+3*w)
    star(sx+2*w,sy,sx+3*w,sy+w)
    star(sx+2*w,sy+w,sx+3*w,sy+2*w)
    star(sx+2*w,sy+2*w,ex,ey)

star(0,0,N,N)
for row in ans:
    for s in row:
        if s == 0:
            print(end=' ')
            continue
        print(s,end='')
    print()