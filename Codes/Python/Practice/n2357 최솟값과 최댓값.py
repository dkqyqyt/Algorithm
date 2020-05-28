def init_min(l,r,node):
    if l == r:
        tree_min[node] = nums[l]
        return tree_min[node]
    mid = (l+r)//2
    tree_min[node] = min(init_min(l,mid,node*2), init_min(mid+1,r,node*2+1))
    return tree_min[node]

def find_min(l,r,node,nodeL,nodeR):
    if l > nodeR or r < nodeL:
        return 1000000001
    if l <= nodeL and r >= nodeR:
        return tree_min[node]

    mid = (nodeL + nodeR)//2
    return min(find_min(l,r,node*2,nodeL,mid), find_min(l,r,node*2+1,mid+1,nodeR))

def init_max(l,r,node):
    if l == r:
        tree_max[node] = nums[l]
        return tree_max[node]
    mid = (l+r)//2
    tree_max[node] = max(init_max(l,mid,node*2), init_max(mid+1,r,node*2+1))
    return tree_max[node]

def find_max(l,r,node,nodeL,nodeR):
    if l > nodeR or r < nodeL:
        return 0
    if l <= nodeL and r >= nodeR:
        return tree_max[node]

    mid = (nodeL + nodeR)//2
    return max(find_max(l,r,node*2,nodeL,mid), find_max(l,r,node*2+1,mid+1,nodeR))

n, m = map(int,input().split())

tree_min = [0] * 500001
tree_max = [0] * 500001
nums = []

for i in range(n):
    nums.append(int(input()))

init_min(0,n-1,1)
init_max(0,n-1,1)

for i in range(m):
    a,b = map(int,input().split())
    print(find_min(a-1,b-1,1,0,n-1), end= ' ')
    print(find_max(a-1,b-1,1,0,n-1))