import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline()
pattern = ''
cur, cnt, res = 0, 0, 0

while cur < (M-1):
    if S[cur:cur+3] == 'IOI':
        cnt += 1
        cur += 2
        if cnt == N:
            res += 1
            cnt -= 1
    else:
        cur += 1
        cnt = 0
print(res)