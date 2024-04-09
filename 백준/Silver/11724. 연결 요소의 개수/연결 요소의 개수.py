import sys
sys.setrecursionlimit(10000000)

N, M = map(int, sys.stdin.readline().split())
network = [[] for _ in range(N+1)]
visitied = [False] * (N+1)
count = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    network[a].append(b)
    network[b].append(a)

def dfs(x):
    visitied[x] = True
    for i in network[x]:
        if visitied[i] == False:
            dfs(i)

for j in range(1, N+1):
    if visitied[j] == False:
        dfs(j)
        count += 1

print(count)