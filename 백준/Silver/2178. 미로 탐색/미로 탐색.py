import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[0] * (M+2)]
visited = [[False for _ in range(M+2)] for _ in range(N+2)]
visited[1][1] = True
direction = [(1,0), (-1,0), (0,1), (0,-1)]
que = deque()

for _ in range(N):
    line = [0]
    line.extend(list(map(int, input())))
    line.append(0)
    graph.append(line)
graph.extend([[0] * (M+2)])

que.append((1,1))

while que:
    x, y = que.popleft()
    if x == N and y == M:
        print(graph[x][y])
        break
    for i in range(4):
        nx, ny = x + direction[i][0], y + direction[i][1]
        if graph[nx][ny] != 0 and visited[nx][ny] == False:
            visited[nx][ny] = True
            graph[nx][ny] += graph[x][y]
            que.append((nx,ny))