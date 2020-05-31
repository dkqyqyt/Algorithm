import heapq

def init():
    for i in range(1,n+1):
        if not indegree[i]:
            heapq.heappush(que,i)

def lineup():
    while que:
        student = heapq.heappop(que)
        print(student, end = ' ')
        for i in range(len(students[student])):
            next_stu = students[student][i]

            indegree[next_stu] -= 1
            if not indegree[next_stu]:
                heapq.heappush(que,next_stu)

n, m = map(int,input().split())

students = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
que = []

for i in range(m):
    a, b = map(int,input().split())
    students[a].append(b)
    indegree[b] += 1

init()
lineup()

