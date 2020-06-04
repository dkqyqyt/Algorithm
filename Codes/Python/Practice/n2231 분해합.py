n = int(input())
for i in range(n):
    num = i
    mysum = i
    while num:
        mysum += num%10
        num //= 10
    if mysum == n:
        print(i)
        break
else:
    print(0)