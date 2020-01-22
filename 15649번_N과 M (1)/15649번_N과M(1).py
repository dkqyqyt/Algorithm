user_input = input()

N, M = map(int,user_input.split(' '))
numbers = list(range(1,N+1))

def track(start,depth,ans):
    if depth == M-1:
        result = list(map(str,ans))
        print(' '.join(result))
        return
    for number in numbers:
        if ans is not None:
            if number in ans:
                continue
            else:
                ans.append(number)
                track(number,depth+1,ans)
                ans.pop()
        
    

for number in numbers:
    track(number,0,[number])