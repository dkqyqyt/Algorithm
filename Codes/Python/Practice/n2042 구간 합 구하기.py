def sum(l,r,node_num,nodeL,nodeR):
    if r < nodeL or nodeR < l:
        return 0
    if l <= nodeL and r >= nodeR:
        return tree[node_num]
    mid = (nodeL+nodeR)//2
    return sum(l,r,node_num*2, nodeL,mid)+sum(l,r,node_num*2+1,mid+1,nodeR)

def init(node_num, start, end):
    if start == end:
        tree[node_num] = nums[start]
        return tree[node_num]
    tree[node_num] = init(node_num*2, start, (start+end)//2) + init(node_num*2+1,(start+end)//2+1,end)
    return tree[node_num]

def update(nodeNum, idx, start, end, diff):
    if idx < start or idx > end:
        return
    tree[nodeNum] += diff

    if start != end:
        update(nodeNum*2,idx,start,(start+end)//2, diff)
        update(nodeNum*2 + 1, idx, (start+end)//2+1,end,diff)

n,m,k = map(int,input().split())

nums = []

for i in range(n):
    nums.append(int(input()))

tree = [0]*3000000
init(1,0,n-1)
# print(tree[:16])
for i in range(m+k):
    do, a, b = map(int,input().split())

    if do == 1:
        diff = b-nums[a-1]
        nums[a-1] = b
        update(1,a-1,0,n-1,diff)
    else:
        print(sum(a-1,b-1,1,0,n-1))