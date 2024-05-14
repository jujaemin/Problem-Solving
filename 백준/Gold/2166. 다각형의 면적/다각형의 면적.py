import sys

T = int(sys.stdin.readline())
dots = []
area1, area2 = 0, 0

for _ in range(T):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    dots.append((x,y))

for i in range(T-1):
    area1 += dots[i][0] * dots[i+1][1]
    area2 += dots[i][1] * dots[i+1][0]

area1 += dots[-1][0] * dots[0][1]
area2 += dots[-1][1] * dots[0][0]

area = round(abs(area1-area2)/2, 1)

print(area)