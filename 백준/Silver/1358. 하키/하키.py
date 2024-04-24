import sys
import math

W, H, X, Y, P = map(int, sys.stdin.readline().split())
athletes = 0

for _ in range(P):
    x,y = map(int, sys.stdin.readline().split())
    if (X <= x <= X+W and Y <= y <= Y+H) or (math.sqrt(((X-x)**2)+(((Y+(H/2))-y)**2)) <= (H/2)) or (math.sqrt((((X+W)-x)**2)+(((Y+(H/2))-y)**2)) <= (H/2)):
        athletes += 1

print(athletes)