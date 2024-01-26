import sys


N = int(sys.stdin.readline())
answer = []

for _ in range(N):
    M = int(sys.stdin.readline())
    test = [i for i in range(1, M+1)]

    el = list(map(int, input().split()))

    for i in range(len(test)):
        if test[i] == el[i]:
            test[i] += 1
    
        for j in range(i+1, len(test)):
            if test[j-1] >= test[j]:
                test[j] = test[j-1]+1
    
    answer.append(test[-1])

for ans in answer:
    print(ans)