import sys
import math

T = int(sys.stdin.readline())

for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int, sys.stdin.readline().split())
    distance_c = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    distnace_r = r1+r2

    if (x1 == x2) and (y1 == y2):
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if abs(r2 - r1) < distance_c < distnace_r:
            print(2)
        elif distance_c == distnace_r or distance_c == abs(r2 - r1):
            print(1)
        else:
            print(0)