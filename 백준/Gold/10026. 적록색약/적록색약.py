import sys

sys.setrecursionlimit(10000000)
N = int(sys.stdin.readline())
board = []
visited = [[False for _ in range(N)] for _ in range(N)]
direction = [(1,0),(-1,0),(0,-1),(0,1)]
normal, blind = 0, 0

for _ in range(N):
    line = list(input())
    board.append(line)


def dfs(x,y):
    visited[x][y] = True
    cur_color = board[x][y]
    for k in range(4):
        nx, ny = x+direction[k][0], y+direction[k][1]
        if (0 <= nx < N) and (0 <= ny < N):
            if visited[nx][ny] == False and board[nx][ny] == cur_color:
                dfs(nx,ny)

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i,j)
            normal += 1

for l in range(N):
    for m in range(N):
        if board[l][m] == 'R':
            board[l][m] = 'G'

visited = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i,j)
            blind += 1

print(normal, blind)