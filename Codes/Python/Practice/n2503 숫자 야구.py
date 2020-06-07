check = [1 for _ in range(1000)]

def strike_ball(num):
    num = str(num)
    s = 0
    b = 0
    for i in range(3):
        for j in range(3):
            if num[i] == num_call[j]:
                if i == j:
                    s += 1
                else:
                    b += 1
    return s,b

n = int(input())

for _ in range(n):
    num_call, s, b = input().split()
    for i in range(100,1000):
        if not check[i]:
            continue
        i = str(i)
        if i[0] == i[1] or i[1] == i[2] or i[0] == i[2] or int(i[1]) == 0 or int(i[2]) == 0:
            check[int(i)] = 0
            continue
        i = int(i)
        strike, ball = strike_ball(i)
        if int(s) == strike and int(b) == ball:
            continue
        else:
            check[i] = 0
cnt = 0
for i in range(100,1000):
    if check[i]:
        cnt += 1
print(cnt)