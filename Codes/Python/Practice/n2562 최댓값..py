maxn = 0
max_index = 0
for i in range(9):
    num = int(input())

    if num > maxn:
        maxn = num
        max_index = i

print(maxn)
print(max_index+1)