n = int(input())

memo = [[0,0] for _ in range(n+1)]

memo[1][1] = 1
for i in range(2,n+1):
    memo[i][0] = memo[i-1][0] + memo[i-1][1]
    memo[i][1] = memo[i-1][0]

print(memo[n][0]+memo[n][1])