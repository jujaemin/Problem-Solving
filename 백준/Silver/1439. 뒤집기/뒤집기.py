import sys

S = sys.stdin.readline()
cnt_one, cnt_zero = 0, 0
n = len(S)
answer = 0

for i in range(n-1):
    if S[i] != S[i+1] and S[i] == '1':
        cnt_one += 1
    elif S[i] != S[i+1] and S[i] == '0':
        cnt_zero += 1

if S[n-1] != S[n-2] and S[n-1] == '1':
    cnt_one += 1
elif S[n-1] != S[n-2] and S[n-1] == '0':
    cnt_zero += 1

if cnt_one == 0 or cnt_zero == 0:
    print(answer)
else:
    answer = min(cnt_one, cnt_zero)
    print(answer)