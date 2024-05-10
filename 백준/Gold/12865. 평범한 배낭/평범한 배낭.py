import sys

N, K = map(int, sys.stdin.readline().split())
take = []
dp = [0] * (K+1)

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    take.append((W,V))

for w,v in take:
    for i in range(K,w-1,-1):
        dp[i] = max(dp[i-w]+v, dp[i])

print(dp[K])