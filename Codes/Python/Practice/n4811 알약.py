def track(w, h):
    global cnt
    if w == 0 and h == 0:
        cnt += 1
        return
    if w != 0:
        track(w-1,h+1)
    if h != 0:
        track(w,h-1)

while True:
    cnt = 0
    N = int(input())
    if N == 0:
        break
    track(N,0)
    print(cnt)


