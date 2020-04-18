from collections import deque
import sys

opers = ['+','-','*']
N = int(input())
maxn = -987654321
expressions = input()
ex = []

for i in range(len(expressions)):
    if i % 2 == 0:
        ex.append(int(expressions[i]))
    else:
        ex.append(expressions[i])

def cal(num1, num2, oper):
    if oper == '+':
        return num1+num2
    elif oper == '-':
        return num1-num2
    else:
        return num1*num2

def cal_all(que):
    idx = 0
    result = que[idx]
    while idx < len(que)-2:
        result = cal(result,que[idx+2],que[idx+1])
        idx += 2
    return result

def track(idx,que):
    global maxn
    if idx == N-1:
        do = False
        if que[-1] in opers:
            do = True
            que.append(ex[idx])
        tmp = cal_all(que)
        if tmp > maxn:
            maxn = tmp
        if do:
            que.pop()
        return
    elif idx > N-1:
        return

    que.append(ex[idx])
    que.append(ex[idx+1])
    track(idx+2,que)
    que.pop()
    que.pop()

    if idx == N-3:
        que.append(cal(ex[idx],ex[idx+2],ex[idx+1]))
        track(idx+2,que)
        que.pop()
    else:
        que.append(cal(ex[idx],ex[idx+2],ex[idx+1]))
        que.append(ex[idx+3])
        track(idx+4,que)
        que.pop()
        que.pop()

if len(expressions) == 1:
    print(expressions)
    sys.exit(0)
q = deque()
track(0,q)
print(maxn)