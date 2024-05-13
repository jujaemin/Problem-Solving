import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    visited = [False] * 10001
    que = deque()

    que.append((A,''))
    visited[A] = True

    while que:
        num, act = que.popleft()

        if num == B:
            print(act)
            break
            
        n1,n2,n3,n4 = (num*2)%10000, (num-1)%10000, (num%1000)*10+num//1000, (num%10)*1000+num//10
        
        if not visited[n1]:
            que.append((n1, act+'D'))
            visited[n1] = True
        
        if not visited[n2]:
            que.append((n2, act+'S'))
            visited[n2] = True
        
        if not visited[n3]:
            que.append((n3, act+'L'))
            visited[n3] = True
        
        if not visited[n4]:
            que.append((n4, act+'R'))
            visited[n4] = True