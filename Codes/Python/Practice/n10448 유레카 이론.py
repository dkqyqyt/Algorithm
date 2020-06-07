num = 1
tri_num = []
while (num*(num+1))/2 <= 1000:
    tri_num.append(num*(num+1)//2)
    num += 1

TCs = int(input())

for tc in range(TCs):
    num = int(input())
    flag = False
    for i in range(len(tri_num)):
        for j in range(len(tri_num)):
            for k in range(len(tri_num)):
                mysum = tri_num[i] + tri_num[j] + tri_num[k]
                if mysum == num:
                    flag = True
                    break
            if flag:
                break
        if flag:
            break

    if flag:
        print(1)
    else:
        print(0)
