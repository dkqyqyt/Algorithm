def gcd(m,n):
    if n == 0:
        return m
    return gcd(n,m%n)

tc = int(input())

for _ in range(tc):
    nums = list(map(int,input().split()))
    ans = 0
    for i in range(1,len(nums)):
        for j in range(i+1,len(nums)):
            ans += gcd(nums[i],nums[j])
    print(ans)