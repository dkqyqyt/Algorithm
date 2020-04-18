import sys

TCs = int(sys.stdin.readline())

for tc in range(TCs):
    len_arr,len_code,len_word = map(int,sys.stdin.readline().split())

    arr = [0] * len_arr
    loop = [0] * len_code
    code = list(sys.stdin.readline())
    word = list(sys.stdin.readline())

    idx = 0
    word_idx = 0
    code_idx = 0
    stack = []
    cnt = 0

    for i in range(len_code):
        if code[i] == '[':
            stack.append(i)
        elif code[i] == ']':
            loc = stack.pop()
            loop[i] = loc
            loop[loc] = i
    max_index = 0
    while True:
        if code[code_idx] == '+':
            arr[idx] = (arr[idx]+1) % 256
            code_idx += 1
        elif code[code_idx] == '-':
            if arr[idx] == 0:
                arr[idx] = 255
            else:
                arr[idx] = (arr[idx]-1)%256
            code_idx += 1
        elif code[code_idx] == '<':
            if idx-1 < 0:
                idx = len_arr - 1
            else:
                idx -= 1
            code_idx += 1
        elif code[code_idx] == '>':
            if idx + 1 >= len_arr:
                idx = 0
            else:
                idx += 1
            code_idx += 1
        elif code[code_idx] == '[':
            if arr[idx] == 0:
                code_idx = loop[code_idx]
            code_idx += 1
        elif code[code_idx] == ']':
            if arr[idx] != 0:
                code_idx = loop[code_idx]
            else:
                code_idx += 1
        elif code[code_idx] == ',':
            if word_idx >= len_word:
                arr[idx] = 255
            else:
                arr[idx] = ord(word[word_idx])
                word_idx += 1
            code_idx += 1
        else:
            code_idx += 1
        cnt += 1

        if code_idx > max_index:
            max_index = code_idx

        if code_idx == len_code:
            print('Terminates')
            break

        if cnt > 50000000:
            print('Loops %d %d'%(loop[max_index], max_index))
            break
