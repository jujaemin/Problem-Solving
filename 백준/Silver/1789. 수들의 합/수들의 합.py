import sys

S = int(sys.stdin.readline())
cnt, i = 0, 1
if S == 1:
    cnt = 1
else:
    while S >= i:
        S -= i
        cnt += 1
        i += 1

print(cnt)