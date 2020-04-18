K = int(input())

stack = []
for i in range(K):
    num = int(input())

    if num == 0:
        stack.pop()
        continue
    stack.append(num)

if stack:
    print(sum(stack))
else:
    print(0)