from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[1 for _ in range(102)] for _ in range(102)]
    direction = [(-1,0),(0,1),(1,0),(0,-1)]
    que = deque()

    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: 2*x, r)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1
    
    cx, cy, ix, iy = characterX*2, characterY*2, itemX*2, itemY*2
    que.append([cx,cy])

    while que:
        x, y = que.popleft()
        if x == ix and y == iy:
            answer = visited[x][y] // 2
        for k in range(4):
            nx, ny = x + direction[k][0], y + direction[k][1]
            if graph[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] += visited[x][y]
                que.append([nx,ny])

    return answer