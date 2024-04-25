import sys

K = int(sys.stdin.readline())
spot = []
x,y = 0,0
x_left, x_right, y_top, y_bottom = 0, 0, 0, 0
c_x, c_y = 0, 0
east, west, south, north = 0, 0, 0, 0
long_len, short_len, long_hei, short_hei = 0, 0, 0, 0

for _ in range(6):
    dir, length = map(int, sys.stdin.readline().split())

    if dir == 1:
        x = x + length
        east += 1
        spot.append([x,y])
    elif dir == 2:
        x = x - length
        west += 1
        spot.append([x,y])
    elif dir == 3:
        y = y - length
        south += 1
        spot.append([x,y])
    elif dir == 4:
        y = y + length
        north += 1
        spot.append([x,y])

for s in spot:
    if s[0] > x_right:
        x_right = s[0]
    if s[0] < x_left:
        x_left = s[0]
    if s[1] > y_top:
        y_top = s[1]
    if s[1] < y_bottom:
        y_bottom = s[1]

long_len = x_right - x_left
long_hei = y_top - y_bottom

for s in spot:
    if x_left < s[0] < x_right:
        c_x = s[0]
    if y_bottom < s[1] < y_top:
        c_y = s[1]

if west == 2 and north == 2:
    short_len = x_right-c_x
    short_hei = y_top-c_y
elif west == 2 and south == 2:
    short_len = c_x-x_left
    short_hei = y_top-c_y
elif east == 2 and south == 2:
    short_len = c_x-x_left
    short_hei = c_y-y_bottom
elif east == 2 and north == 2:
    short_len = x_right-c_x
    short_hei = c_y-y_bottom

print(K*((long_hei*long_len)-(short_hei*short_len)))