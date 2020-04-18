primes = [True]*1000001
def Eratos():
    m = int(1000000**0.5)
    for i in range(2,m+1):
        if primes[i]:
            for j in range(i*2,1000001,i):
                primes[j] = False

Eratos()
# for i in range(len(primes)):
#     print(i,primes[i])

while True:
    num = int(input())

    if num == 0:
        break

    for i in range(3,num//2+1,2):
        if not primes[i]:
            continue
        if not primes[num-i]:
            continue
        print('%d = %d + %d'%(num,i,num-i))
        break