import sys

N = int(sys.stdin.readline())
weights = []

for _ in range(N):
    weight = int(sys.stdin.readline().rstrip())
    weights.append(weight)

weights.sort()
for i in range(N,0,-1):
    weights[N-i] = weights[N-i]*i

print(max(weights))