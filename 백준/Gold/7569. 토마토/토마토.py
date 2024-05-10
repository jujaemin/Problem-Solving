import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
field = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
direction = ((1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1))
que = deque()

for k in range(H):
    for i in range(N):
        for j in range(M):
            if field[k][i][j] == 1:
                visited[k][i][j] = True
                que.append((k,i,j))

def bfs():
    cnt = 0

    while que:
        z,y,x = que.popleft()

        for m in range(6):
            nx,ny,nz = x+direction[m][0],y+direction[m][1],z+direction[m][2]

            if (0 <= nz < H) and (0 <= ny < N) and (0 <= nx < M):
                if field[nz][ny][nx] != -1 and visited[nz][ny][nx] == False:
                    visited[nz][ny][nx] = True
                    field[nz][ny][nx] = field[z][y][x]+1
                    que.append((nz,ny,nx))
    
    for k in range(H):
        for i in range(N):
            for j in range(M):

                if field[k][i][j] == 0:
                    return -1
                
                else:
                    cnt = max(cnt,field[k][i][j])
    return cnt-1


print(bfs())