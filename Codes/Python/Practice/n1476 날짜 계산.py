e,s,m = map(int,input().split())
esm = [0]*3

year = 0
while True:
    year += 1
    for i in range(len(esm)):
        esm[i] += 1

    if esm[0] > 15:
        esm[0] = 1
    if esm[1] > 28:
        esm[1] = 1
    if esm[2] > 19:
        esm[2] = 1

    if esm[0] == e and esm[1] == s and esm[2] == m:
        break

print(year)
