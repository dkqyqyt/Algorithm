# 17509번 And the Winner is ... Ourselves!

| 시간 제한             | 메모리 제한 | 제출 | 정답 | 맞은 사람 | 정답 비율 |
| :-------------------- | :---------- | :--- | :--- | :-------- | :-------- |
| 4 초 (추가 시간 없음) | 1024 MB     | 209  | 174  | 168       | 90.811%   |

## 문제

Let us remind you about how the total penalties are calculated for this contest:

- When you solve a problem at T minutes, T+20V is added to your penalty, where V is the number of incorrect verdicts (except compile errors) received on that problem.
- If you do not solve a problem before the contest ends, the incorrect verdicts on that problem are not counted as penalties.

Here is a bad news for all of you: we, the problem setters, are planning to join the competition and solve our own problems!

We know our problems really well, so we can solve all the problems before the contest ends. Furthermore, we can precisely predict how long it takes to solve each problem, and how many incorrect verdicts (except compile errors) we get in each problem. Depending on the order of the problems we solve, our total penalty might differ. What is the minimum penalty if we solve all problems?

## 입력

11 lines are given as the input. The i-th line contains two space-separated integers, Di and Vi, where Di is the amount of minutes required to solve the i-th problem, and Vi is the number of incorrect verdicts on the i-th problem.

For each i, 1≤Di and 0≤Vi≤1 000. Also, ∑i=111Di≤300.

## 출력

Output the minimum penalty if we solve all problems.

## 예제 입력 1 

```
20 1
20 0
20 3
10 0
10 0
10 0
30 0
30 0
30 0
20 0
20 10
```

## 예제 출력 1 

```
1360
```

## 나의 코드

```
times = []

for i in range(11):# ddd
    info = list(map(int,input().split()))
    times.append(info)
times.sort()

time = 0
verdicts= 0
ans = 0
for i in range(len(times)):
    time += times[i][0]
    ans += time
    verdicts += times[i][1]

ans += verdicts*20
print(ans)
```

