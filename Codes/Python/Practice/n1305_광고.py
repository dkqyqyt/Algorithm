L = int(input())

input_word = input()
words = []
for word in input_word:
    words.append(word)


i = 0
j = 0
Pi = [0 for _ in range(len(words))]
Pi[0] = 0

for i in range(1,len(words)):
    while j > 0 and words[i] != words[j]:
        j = Pi[j - 1]

    if words[i] == words[j]:
        Pi[i] = j + 1
        j += 1
    else:
        Pi[i] = 0
print(Pi)
print(L-Pi[len(words)-1])