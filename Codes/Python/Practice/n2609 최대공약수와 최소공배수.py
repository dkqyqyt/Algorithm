def gcd(m,n):
    if n == 0:
        return m
    return gcd(n,m%n)

m,n = map(int,input().split())

gcd = gcd(m,n)
print(gcd)
print(m*n//gcd)