from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [False for _ in range(len(words))]
    que = deque()
    
    que.append([begin, 0])
    
    while que:
        word, cnt = que.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            temp = 0
            if visited[i] == False:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp += 1
                if temp == 1:
                    cnt += 1
                    que.append([words[i], cnt])
                    visited[i] = True
    return answer