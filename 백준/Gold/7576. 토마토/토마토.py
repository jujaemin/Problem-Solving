import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]
que = deque()

for i in range(N):
    for j in range(M):
        if field[i][j] == 1:
            visited[i][j] = True
            que.append((i,j))


def bfs():
    cnt = 0
    while que:
        x,y = que.popleft()

        for k in range(4):
            nx,ny = x+direction[k][0],y+direction[k][1]

            if (0 <= nx < N) and (0 <= ny < M) and visited[nx][ny] == False:
                if field[nx][ny] != -1:
                    field[nx][ny] = field[x][y] + 1
                    visited[nx][ny] = True
                    que.append((nx, ny))
    
    for i in range(N):
        for j in range(M):
            if field[i][j] == 0:
                return -1
            
            else:
                cnt = max(cnt, field[i][j])
    return cnt-1
    
print(bfs())