import sys
from collections import deque

N,M,V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)
dfs_result = []
bfs_result = []
que = deque()

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for gr in graph:
    gr.sort()

def dfs(x):
    dfs_visited[x] = True
    dfs_result.append(str(x))

    for i in graph[x]:
        if dfs_visited[i] == False:
            dfs(i)

def bfs():
    while que:
        y = que.popleft()
        for j in graph[y]:
            if bfs_visited[j] == False:
                bfs_visited[j] = True
                bfs_result.append(str(j))
                que.append(j)

que.append(V)
bfs_visited[V] = True
bfs_result.append(str(V))

dfs(V)
bfs()

print(' '.join(dfs_result))
print(' '.join(bfs_result))