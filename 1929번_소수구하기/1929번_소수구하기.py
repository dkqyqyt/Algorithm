# def primeNum(num):
#     for i in range(2,num):
#         if num%i == 0:
#             return False
#     return True

# M, N = map(int,input().split(' '))

# for i in range(M,N+1):
#     if primeNum(i):
#         print(i)

#에라토스테네스의 체
M,N = map(int,input().split(' '))

numbers = [True]*(N+1)
numbers[1] = False

for i in range(2,round(N**0.5+0.5)):
    if numbers[i]:
        cnt = 2
        while(cnt * i <= N):
            numbers[cnt*i] = False
            cnt += 1

for i in range(M,N+1):
    if numbers[i]:
        print(i)
                    