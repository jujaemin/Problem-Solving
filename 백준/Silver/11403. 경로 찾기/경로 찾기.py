import sys
import math

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


for a in range(N):
    graph[a][a] = 0

for i in range(N):
    for j in range(N):
            for k in range(N):
                if graph[j][i] == 1 and graph[i][k] == 1:
                    graph[j][k] = 1

for gr in graph:
    for m in range(len(gr)):
        gr[m] = str(gr[m])
    print(' '.join(gr))
