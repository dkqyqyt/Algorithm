hanoy_tower = []*4

def move(source, target):
    print(source, target)
    # hanoy_tower[source] -= 1
    # hanoy_tower[target] += 1  

def hanoy(source, target, extra, size):
    if size == 1:
        move(source,target)
        return
    hanoy(source, extra, target,size-1)
    move(source, target)
    hanoy(extra,target,source,size-1)

num = int(input())
print(2**num -1)
hanoy(1,3,2,num)