import sys
from collections import deque

sys.setrecursionlimit(10000000)
N = int(sys.stdin.readline())
town = []
visited = [[False for _ in range(N)] for _ in range(N)]
direction = [(1,0),(-1,0),(0,-1),(0,1)]
que = deque()
section = 0
result = []

for _ in range(N):
    line = list(map(int,sys.stdin.readline().rstrip()))
    town.append(line)

def bfs():
    cnt = 1
    while que:
        x,y = que.popleft()
        for k in range(4):
            nx, ny = x+direction[k][0], y+direction[k][1]
            if (0 <= nx < N) and (0 <= ny < N):
                if visited[nx][ny] == False and town[nx][ny] == 1:
                    cnt += 1
                    visited[nx][ny] = True
                    que.append([nx,ny])
    return cnt

for i in range(N):
    for j in range(N):
        if town[i][j] == 1 and visited[i][j] == False:
            que.append([i,j])
            visited[i][j] = True
            res = bfs()
            result.append(res)
            section += 1

result.sort()
print(section)
for m in result:
    print(m)