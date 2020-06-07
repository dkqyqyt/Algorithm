n,k = map(int,input().split())

multitab = []

order = list(map(int,input().split()))
cnt = 0

for i in range(len(order)):
    multitab.sort()
    next_use = 101
    for j in range(i+1,len(order)):
        if order[j] == order[i]:
            next_use = j
            break

    if not multitab:
        multitab.append([next_use,order[i]])
        continue
    flag = False
    for j in range(len(multitab)):
        if multitab[j][1] == order[i]:
            multitab[j][0] = next_use
            flag = True
            break
    if flag:
        continue
    if len(multitab) < n:
        multitab.append([next_use,order[i]])
        continue

    multitab.pop()
    cnt += 1
    multitab.append([next_use,order[i]])

print(cnt)



