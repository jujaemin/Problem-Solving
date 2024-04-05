import sys

sys.setrecursionlimit(3000)
T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    ground = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    direction = [(1,0),(-1,0),(0,-1),(0,1)]
    warm = 0

    for _ in range(K):
        cabbage_col, cabbage_row = map(int, sys.stdin.readline().split())
        ground[cabbage_row][cabbage_col] = 1
    
    def dfs(x,y):
        visited[x][y] = True
        for k in range(4):
            nx, ny = x+direction[k][0], y+direction[k][1]
            if (0 <= nx < N) and (0 <= ny < M):
                if visited[nx][ny] == False and ground[nx][ny] == 1:
                    dfs(nx,ny)
    
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1 and visited[i][j] == False:
                dfs(i,j)
                warm += 1
    
    print(warm)