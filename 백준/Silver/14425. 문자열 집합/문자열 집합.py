import sys

N, M = map(int, sys.stdin.readline().split())
S = {}
result = 0

for _ in range(N):
    S[sys.stdin.readline().rstrip()] = True

for _ in range(M):
    string = sys.stdin.readline().rstrip()
    if string in S.keys():
        result += 1

print(result)