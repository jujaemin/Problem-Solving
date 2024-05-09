import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
que = deque()
result = []

for i in range(1, N+1):
    que.append(i)

while que:
    que.rotate(-(K-1))
    result.append(str(que.popleft()))
print('<'+ ', '.join(result)+'>')