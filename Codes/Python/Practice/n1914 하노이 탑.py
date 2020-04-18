N = int(input())

def move(source, target, storage, n):
    if n == 0:
        return
    move(source, storage, target, n-1)
    print(source, target)
    move(storage, target, source, n-1)

ans = (1<<N)-1

print(ans)
if N <= 20:
    move(1,3,2,N)