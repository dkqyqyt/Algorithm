TCs = int(input())

def track(depth, score, path):
    global max_score

    if depth == 11:
        # print(path, score)
        if score > max_score:
            max_score = score
        return

    for i in range(11):
        if used[i]:
            continue

        if graph[depth][i] == 0:
            continue

        used[i] = 1
        path.append(i)
        track(depth+1, score + graph[depth][i], path)
        used[i] = 0
        path.pop()

for tc in range(TCs):
    score = 0
    max_score = 0

    used = [0]*11
    graph = []

    for i in range(11):
        graph.append(list(map(int,input().split())))

    track(0,score, [])
    print(max_score)

