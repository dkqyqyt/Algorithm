import sys
from itertools import permutations

N = int(sys.stdin.readline())

Info = []
for i in range(N):
    Info.append(list(map(int,sys.stdin.readline().split())))

def play(order):
    hitter_idx = 0
    score = 0
    for inn in range(N):
        out = 0
        b1,b2,b3 = 0,0,0
        while out < 3:
            if Info[inn][order[hitter_idx]] == 0:
                out += 1
            elif Info[inn][order[hitter_idx]] == 1:
                score += b3
                b1,b2,b3 = 1,b1,b2
            elif Info[inn][order[hitter_idx]] == 2:
                score += (b2+b3)
                b1, b2, b3 =0, 1, b1
            elif Info[inn][order[hitter_idx]] == 3:
                score += (b1+b2+b3)
                b1, b2, b3 = 0,0,1
            elif Info[inn][order[hitter_idx]] == 4:
                score += (b1+b2+b3+1)
                b1, b2, b3 = 0,0,0
            hitter_idx = (hitter_idx + 1) % 9
    return score
max_score = 0

for order in permutations(range(1,9),8):
    order = list(order[:3]) + [0] + list(order[3:])
    max_score = max(play(order),max_score)
print(max_score)