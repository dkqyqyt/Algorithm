# import sys
# sys.setrecursionlimit(10**9)
#
# def tile(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     if memo[n]:
#         return memo[n]
#
#     result = (tile(n-1) + tile(n-2))%15746
#     memo[n] = result
#     return result

n = int(input())

memo = [0 for _ in range(1000001)]
memo[0] = 1
memo[1] = 1

for i in range(2,n+1):
    memo[i] = (memo[i-1] + memo[i-2])%15746

print(memo[n])

# print(tile(n))