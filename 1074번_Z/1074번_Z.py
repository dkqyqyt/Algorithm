# import sys
# sys.setrecursionlimit(10**6)

user_input = input()

N, r, c = map(int,user_input.split(' '))
cnt = 0
found = False

def explore(size, x, y):
    global found
    global cnt

    if found :
        return

    if size == 2:
        if x == r and y == c:
            found = True
            return   
        # print(cnt)        
        cnt += 1

        if x == r and y + 1 == c:
            found = True
            return
        # print(cnt)
        cnt += 1
 
        if x + 1 == r and y == c:
            found = True
            return
        # print(cnt)
        cnt += 1

        if x + 1 == r and y + 1== c:
            found = True
            return
        # print(cnt)
        cnt += 1
        return


    explore(int(size/2), x, y)
    explore(int(size/2), x, y + int(size/2))
    explore(int(size/2), x + int(size/2), y)
    explore(int(size/2), x + int(size/2), y + int(size/2))

explore(1<<N, 0, 0)

print(cnt)