import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def do(x):
    visited[x] = True
    for i in graph[x]:
        if visited[i] == False:
            do(i)

do(1)

print(visited.count(True)-1)