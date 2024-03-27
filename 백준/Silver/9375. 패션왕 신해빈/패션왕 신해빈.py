import sys

N = int(sys.stdin.readline())

for _ in range(N):
    dic = {}
    answer = 1
    K = int(sys.stdin.readline())

    for i in range(K):
        cloth,category = map(str, sys.stdin.readline().split())
        dic[category] = dic.get(category, []) + [cloth]
    
    for j in dic:
        answer *= (len(dic[j])+1)
    
    print(answer-1)