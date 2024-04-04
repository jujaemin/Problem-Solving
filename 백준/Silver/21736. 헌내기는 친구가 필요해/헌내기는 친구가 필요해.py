import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
graph = [['X' for _ in range(M+2)]]
visited = [[False for _ in range(M+2)] for _ in range(N+2)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]
que = deque()
cnt = 0

for _ in range(N):
    temp = ['X']
    loc = list(input())
    temp.extend(loc)
    temp.append('X')
    graph.append(temp)
graph.append(['X' for _ in range(M+2)])

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 'I':
            que.append((i,j))
            visited[i][j] = True

while que:
    x, y = que.popleft()
    if graph[x][y] == 'P':
        cnt += 1

    for k in range(4):
        nx, ny = x+direction[k][0], y+direction[k][1]

        if graph[nx][ny] != 'X' and visited[nx][ny] == False:
            visited[nx][ny] = True
            que.append((nx, ny))

if cnt == 0:
    print('TT')
else:
    print(cnt)
