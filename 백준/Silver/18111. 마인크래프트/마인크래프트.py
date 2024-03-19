import sys

row, col, inventory = map(int, sys.stdin.readline().split())
blocks = []

for _ in range(row):
    blocks += list(map(int, sys.stdin.readline().split()))

low = min(blocks)
high = max(blocks)
cnt = sum(blocks)

height, time = 0, row * col * 512

for i in range(high, low-1, -1):

    if cnt + inventory >= row * col * i:
        do_time = 0

        for j in blocks:
            height_dif = i-j

            if height_dif > 0:
                do_time += height_dif

            else:
                do_time -= height_dif * 2
    
        if do_time < time:
            time = do_time
            height = i

print(time, height)
