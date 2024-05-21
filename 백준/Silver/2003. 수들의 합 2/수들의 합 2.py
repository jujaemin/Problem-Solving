import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(N):
    temp = 0
    for j in range(i, N):
        temp += A[j]
        if temp == M:
            cnt += 1
        elif temp > M:
            break

print(cnt)