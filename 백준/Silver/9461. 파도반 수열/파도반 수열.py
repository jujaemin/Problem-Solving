import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    triangle = [0] * 101
    triangle[1] = 1
    triangle[2] = 1
    triangle[3] = 1

    for i in range(4, N+1):
        triangle[i] = triangle[i-2] + triangle[i-3]
    
    print(triangle[N])