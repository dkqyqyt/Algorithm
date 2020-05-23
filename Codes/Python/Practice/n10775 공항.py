import sys
sys.setrecursionlimit(10**6)

def find(node): # Union Find
    if gates[node] == -1:
        return node
    gates[node] = find(gates[node])
    return gates[node]

g = int(input())
p = int(input())

docks = []
for i in range(p):
    docks.append(int(input()))

gates = [-1]*(g+1)

dock_plane = 0

for dock in docks:
    if gates[dock] == -1:
        gates[dock] = dock-1
        dock_plane += 1
    else:
        root = find(dock)
        if root == 0:
            break
        else:
            gates[root] = root-1
            dock_plane += 1

print(dock_plane)