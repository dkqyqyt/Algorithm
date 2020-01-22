user_input = input()

N, M = map(int,user_input.split(' '))

card_input = input()

cards = list(map(int,card_input.split(' ')))

max = 0
iter_stop = False

for i in range(N):
    if iter_stop:
        break
    for j in range(i+1,N):
        if iter_stop:
            break
        for k in range(j+1,N):
            if iter_stop:
                break
            card_sum = cards[i] + cards[j] + cards[k]
            if card_sum  > M:
                iter_stop = True
            elif card_sum > max:
                max = card_sum

print(max)
