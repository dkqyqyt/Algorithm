import sys

N = int(input())

nums = list(map(int,input().split()))

if N <= 2:
    print(N)
    sys.exit(0)

length = 1
max = 0

# bigger
for i in range(len(nums)):
    if i+1 == len(nums):
        if length> max:
            max = length
        length = 1
        break

    if nums[i] <= nums[i+1]:
        length += 1
    else:
        if length > max:
            max = length
        length = 1

# smaller
for i in range(len(nums)):
    if i+1 == len(nums):
        if length> max:
            max = length
        break

    if nums[i] >= nums[i+1]:
        length += 1
    else:
        if length > max:
            max = length
        length = 1

print(max)