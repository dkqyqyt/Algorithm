import sys

costs = input()

A, B, C = map(int,costs.split(' '))

if B >= C :
    ans = -1
else:
    ans = A//(C-B) + 1
1000
print(ans)

