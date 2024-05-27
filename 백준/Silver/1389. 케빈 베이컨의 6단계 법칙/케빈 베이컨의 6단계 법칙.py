import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
relations = [[] for _ in range(N+1)]
result = []

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    if A not in relations[B] and B not in relations[A]:
        relations[A].append(B)
        relations[B].append(A)

def bfs(i):
    que = deque()
    visited = [0] * (N+1)
    que.append(i)

    while que:
        user = que.popleft()
        for r in relations[user]:
            if visited[r] == 0 and r != i:
                visited[r] = visited[user]+1
                que.append(r)
    
    return sum(visited)
            
for i in range(1, N+1):
    result.append([i,bfs(i)])

result.sort(key=lambda x: (x[1],x[0]))

print(result[0][0])