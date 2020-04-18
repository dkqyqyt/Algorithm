def primeNumber(number):
    for i in range(2,number):
        if number%i == 0:
            return False
    return True

N = int(input())
ans = 0
nums = list(map(int,input().split()))

for num in nums:
    if num == 1:
        continue
    if primeNumber(num):
        ans += 1
print(ans)
