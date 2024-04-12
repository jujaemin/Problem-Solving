import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [0] * 100001
hns = [i for i in range(100001)]
que = deque()
que.append(N)

def bfs():
    while que:
        x = que.popleft()
        if hns[x] == K:
            print(visited[x])
            break

        for j in (x-1, x+1, 2*x):
            if (0 <= j <= 100000) and visited[j] == 0:
                visited[j] = visited[x] + 1
                que.append(j)

bfs()