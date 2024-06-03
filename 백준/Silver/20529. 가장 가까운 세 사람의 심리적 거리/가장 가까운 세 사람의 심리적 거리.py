import sys

T = int(sys.stdin.readline())

for _ in range(T):
    distance = 999999
    N = int(sys.stdin.readline())
    mbti = list(sys.stdin.readline().split())

    if N >= 33:
        print(0)
    else:
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    temp = 0
                    for m in range(4):
                        if mbti[i][m] != mbti[j][m]:
                            temp += 1
                        if mbti[j][m] != mbti[k][m]:
                            temp += 1
                        if mbti[k][m] != mbti[i][m]:
                            temp += 1
                    distance = min(distance, temp)
        print(distance)