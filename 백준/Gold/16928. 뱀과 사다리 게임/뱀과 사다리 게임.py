import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [0] * 101
visited = []
que = deque()
lns = {}

for i in range(1, 101):
    lns[i] = i

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    lns[x] = y

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    lns[u] = v

que.append(1)
visited.append(1)

while que:
    die = que.popleft()

    if die >= 100:
        print(board[100])
        break

    for j in range(1, 7):
        nxt = die+j
        if nxt <= 100:
            arrive = lns[nxt]
            if arrive not in visited:
                board[arrive] = board[die]+1
                que.append(arrive)
                visited.append(arrive)