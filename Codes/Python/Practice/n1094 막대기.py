X = int(input())

new_x = str(bin(X))

cnt = 0
for i in range(2, len(new_x)):
    if new_x[i] == '1':
        cnt += 1

print(cnt)
