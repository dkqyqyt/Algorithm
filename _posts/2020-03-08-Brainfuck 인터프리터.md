# 3954번 Brainfuck 인터프리터

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞은 사람 | 정답 비율 |
| :-------- | :---------- | :--- | :--- | :-------- | :-------- |
| 7 초      | 128 MB      | 2155 | 310  | 191       | 13.993%   |

## 문제

Brainf**k 프로그램이 주어졌을 때, 이 프로그램이 끝나는지, 무한 루프에 빠지는지 알아내는 프로그램을 작성하시오.

Brainf**k 인터프리터는 정수를 담는 하나의 배열(unsigned 8-bit 정수)과, 그 배열의 칸 하나를 가리키는 포인터로 이루어져 있다. Brainf**k 프로그램은 다음과 같이 8개의 명령어로 이루어져 있다.

| -    | 포인터가 가리키는 수를 1 감소시킨다. (modulo 28)             |
| :--- | ------------------------------------------------------------ |
| +    | 포인터가 가리키는 수를 1 증가시킨다. (modulo 28)             |
| <    | 포인터를 왼쪽으로 움직인다.(1 감소)                          |
| >    | 포인터를 오른쪽으로 움직인다.(1 증가)                        |
| [    | 만약 포인터가 가리키는 수가 0과 같다면, [와 짝을 이루는 ]로 점프한다. |
| ]    | 만약 포인터가 가리키는 수가 0이 아니라면, ]와 짝을 이루는 [로 점프한다. |
| .    | 포인터가 가리키는 수를 출력한다.                             |
| ,    | 문자 하나를 읽고 포인터가 가리키는 곳에 저장한다. 입력의 마지막(EOF)인 경우에는 255를 저장한다. |

인터프리터는 Brainf**k 프로그램의 첫 번째 명령부터 수행하고, 더이상 수행할 명령이 없다면, 프로그램을 종료한다. 각 명령을 수행하고 나면, 다음 명령을 수행한다. 물론 [이나 ]인 경우에는 다음 명령으로 이동하는 것이 아니라 점프를 한다.

데이터 배열의 크기는 문제에서 주어지는 값을 사용해야 한다. 또, 데이터 배열의 값이 underflow나 overflow를 일으켰을 때는 일반적인 방법을 따르면 된다. 프로그램을 수행하기 전에, 데이터 배열의 값은 0으로 초기화되어 있고, 포인터가 가리키는 칸은 0번 칸이다.

포인터를 왼쪽이나 오른쪽으로 움직일 때, 데이터 배열의 범위를 넘어간다면, 반대쪽으로 넘어가게 된다. 즉, 포인터가 0을 가리킬 때, 1을 감소시킨다면, 배열의 크기 - 1번째를 가리키게 된다.

[와 ]는 루프를 의미하며, 중첩될 수 있다. 입력으로 주어진 프로그램은 잘 짜여 있음이 보장된다. 즉 프로그램을 왼쪽에서 오른쪽으로 훑으면서 [의 개수에서 ]의 개수를 빼면 항상 0보다 크거나 같고, 맨 끝까지 훑으면 그 값은 0이 된다.

이 문제는 Brainf**k 프로그램이 무한 루프에 빠지는지 안 빠지는지를 검사하기만 하면 된다. 따라서, 출력은 무시한다.

## 입력

첫째 줄에 테스트 케이스의 개수 t (0 < t ≤ 20)가 주어진다. 각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 sm, sc, si가 주어진다. sm은 메모리(배열)의 크기이고, sc는 프로그램 코드의 크기, si는 입력의 크기이다. (0 < sm ≤ 100,000, 0 < sc, si < 4096)

둘째 줄에는 Brainf**k 프로그램이 주어진다. 프로그램은 sc개의 문자로 이루어져 있다.

셋째 줄에는 프로그램의 입력이 주어진다. (공백이 아니면서 출력할 수 있는 문자만 주어진다)

## 출력

각 테스트 케이스에 대해서, 프로그램이 종료된다면 "Terminates"를, 무한 루프에 빠지게 된다면 "Loops"를 출력한다. 무한 루프에 빠졌을 때는, 프로그램의 어느 부분이 무한 루프인지를 출력한다. ([와 ]의 위치) 프로그램이 명령어를 50,000,000번 이상 수행한 경우, 프로그램은 항상 종료되었거나 무한 루프에 빠져있다. 무한 루프일 경우, 해당 루프는 적어도 한 번 실행이 완료된 상태이며, 한 번의 무한 루프에서 실행되는 명령어의 개수는 50,000,000개 이하이다.

## 예제 입력 1 

```
4
10 4 3
+-.,
qwe
1000 5 1
+[+-]
a
100 74 4
+++++[->++<]>[-<+++++++>]<[->+>+>+>+<<<<]>+++>--->++++++++++>---<<<.>.>.>.
xxyz
9999 52 14
+++++[>+++++++++<-],+[-[>--.++>+<<-]>+.->[<.>-]<<,+]
this_is_a_test
```

## 예제 출력 1 

```
Terminates
Loops 1 4
Terminates
Terminates
```

## 나의 코드 1

```
import sys

TCs = int(sys.stdin.readline())

for tc in range(TCs):
    len_arr,len_code,len_word = map(int,sys.stdin.readline().split())

    arr = [0] * len_arr
    loop = [0] * len_code
    code = sys.stdin.readline()
    word = sys.stdin.readline()

    idx = 0
    word_idx = 0
    code_idx = 0
    stack = []
    cnt = 0
    infinite = False

    for i in range(len_code):
        if code[i] == '[':
            stack.append(i)
        elif code[i] == ']':
            loc = stack.pop()
            loop[i] = loc
            loop[loc] = i
    max_index = 0
    while True:
        if code_idx > max_index:
            max_index = code_idx

        if code[code_idx] == '+':
            arr[idx] = (arr[idx]+1) % 256
        elif code[code_idx] == '-':
            if arr[idx] == 0:
                arr[idx] = 255
            else:
                arr[idx] = (arr[idx]-1)%256
        elif code[code_idx] == '<':
            if idx-1 < 0:
                idx = len_arr - 1
            else:
                idx -= 1
        elif code[code_idx] == '>':
            if idx + 1 >= len_arr:
                idx = 0
            else:
                idx += 1
        elif code[code_idx] == '[':
            if arr[idx] == 0:
                code_idx = loop[code_idx]
                cnt += 1
                if cnt > 50000000:
                    print('Loops %d %d' % (loop[max_index], max_index))
                    break
                continue
        elif code[code_idx] == ']':
            if arr[idx] != 0:
                code_idx = loop[code_idx]
                cnt += 1
                if cnt > 50000000:
                    print('Loops %d %d' % (loop[max_index], max_index))
                    break
                continue
        elif code[code_idx] == ',':
            if word_idx >= len(word):
                arr[idx] = 255
            else:
                arr[idx] = ord(word[word_idx])
                word_idx += 1
        code_idx += 1
        cnt += 1


        if code_idx == len_code:
            print('Terminates')
            break

        if cnt > 50000000:
            print('Loops %d %d'%(loop[max_index], max_index))
            break
```

이거와 비슷한 코드로 10번 가까이 조금씩 수정해서 제출했는데, 계속 틀렸다고 나왔다. 

BrainFuck 인터프리터에 대해 검색을 해보니 '[' 명령어가 수행될 때 다음 ']'로 건너뛰는 것이 아니라 ']' 다음 명령어로 이동한다고 한다. 

큰 영향이 없을 것 같았는데 저 작은 부분에서 맞았습니다와 틀렸습니다가 차이가 났다...

```
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
```

7440ms 7초의 제한시간에서 조금  더 여유를 받아서 통과하게 된 것 같다.