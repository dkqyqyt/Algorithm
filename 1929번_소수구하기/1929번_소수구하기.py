def primeNum(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

M, N = map(int,input().split(' '))

for i in range(M,N+1):
    if primeNum(i):
        print(i)