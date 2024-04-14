import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
distance = [[0 for _ in range(m)] for _ in range(n)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]
que = deque()
for i in range(n):
    for j in range(m):
        if field[i][j] == 2:
            que.append((i,j))

def bfs():
    while que:
        x,y = que.popleft()

        for k in range(4):
            nx,ny = x+direction[k][0],y+direction[k][1]

            if (0 <= nx < n) and (0 <= ny < m) and distance[nx][ny] == 0:
                
                if field[nx][ny] == 0:
                    distance[nx][ny] == 0
                
                if field[nx][ny] == 1:
                    distance[nx][ny] = distance[x][y]+1
                    que.append((nx,ny))
    
    for i in range(n):
        for j in range(m):
            if distance[i][j] == 0 and field[i][j] == 1:
                distance[i][j] = -1
    
    for i in range(n):
        for j in range(m):
            print(distance[i][j], end=" ")
        print()

bfs()