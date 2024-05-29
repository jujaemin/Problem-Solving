import sys
import math

T = int(sys.stdin.readline())

for _ in range(T):

    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    cnt = 0
    n = int(sys.stdin.readline())
    
    for _ in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        d1, d2 = math.sqrt(((cx-x1)**2)+((cy-y1)**2)), math.sqrt(((cx-x2)**2)+((cy-y2)**2))

        if ((d1 < r) and (d2 > r)) or ((d1 > r) and (d2 < r)):
            cnt += 1
    print(cnt)