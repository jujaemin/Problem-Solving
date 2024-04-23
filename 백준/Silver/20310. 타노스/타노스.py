import sys

S = list(sys.stdin.readline().rstrip())
cnt_0, cnt_1 = S.count('0')//2, S.count('1')//2
n = len(S)

for i in range(n-1,-1,-1):
    if S[i] == '0':
        S.pop(i)
    if S.count('0') == cnt_0:
        break

for j in S:
    if j == '1':
        S.remove(j)
    if S.count('1') == cnt_1:
        break

print(''.join(S))