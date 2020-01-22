N, M = map(int,input().split())
numbers = [i for i in range(1,N+1)]

def track(start,depth,seq):
    seq.append(start)
    if depth == M-1:
        print(*seq)
        return

    for number in numbers:
        if number <= start:
            continue
        track(number,depth+1,seq)
        seq.pop()

for number in numbers:
    track(number,0,[])