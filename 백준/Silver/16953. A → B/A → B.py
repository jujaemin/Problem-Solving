import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())
cnt = 0

while A != B:
    if A > B:
        cnt = -2
        break
    elif B%2 == 0:
        B //= 2
        cnt += 1
    elif int(str(B)[-1]) == 1:
        B = int(str(B)[:-1])
        cnt += 1
    else:
        cnt = -2
        break

print(cnt+1)