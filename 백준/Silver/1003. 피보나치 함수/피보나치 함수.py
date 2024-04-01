import sys

T = int(sys.stdin.readline())

for _ in range(T):
    dp = [[1,0] for _ in range(41)]
    N = int(sys.stdin.readline())

    dp[1] = [0,1]
    dp[2] = [1,1]
    dp[3] = [1,2]

    for i in range(4, N+1):
        dp[i][0] = dp[i-1][1]
        dp[i][1] = dp[i-1][0] + dp[i-1][1]
    
    print(dp[N][0], dp[N][1])