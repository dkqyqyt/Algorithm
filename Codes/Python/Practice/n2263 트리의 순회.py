import sys
sys.setrecursionlimit(10**9)

n = int(input())

in_order = list(map(int,input().split()))
post_order = list(map(int,input().split()))
location = [0 for _ in range(n+1)]
for i in range(len(in_order)):
    location[in_order[i]] = i

tree = [[0,0] for _ in range(n+1)]

def find_tree(in_l, in_r, post_l, post_r):
    if post_l <= post_r:
        parent = post_order[post_r]
        p_index = location[parent]

        l_count = p_index-in_l
        if l_count > 0:
            tree[parent][0] = post_order[post_l + l_count - 1]
        r_count = in_r - p_index
        if r_count > 0:
            tree[parent][1] = post_order[post_r - 1]

        find_tree(in_l, p_index - 1, post_l, post_l + l_count - 1)
        find_tree(p_index+1,in_r, post_l+l_count,post_r -1)

find_tree(0,n-1,0,n-1)
# print(tree)

def pre_order(root):
    print(root, end= ' ')
    if tree[root][0] != 0:
        pre_order(tree[root][0])
    if tree[root][1] != 0:
        pre_order(tree[root][1])

pre_order(post_order[-1])