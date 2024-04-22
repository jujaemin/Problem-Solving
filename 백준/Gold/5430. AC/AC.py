import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    pivot = 0
    answer = ''
    func = sys.stdin.readline()
    length = int(sys.stdin.readline().rstrip())
    arr = deque(sys.stdin.readline().strip()[1:-1].split(','))

    for i in range(len(func)):
        if func[i] == 'R':
            pivot += 1

        if func[i] == 'D':
            if length == 0 or not arr:
                answer = 'error'
                break
            elif pivot%2 == 1:
                arr.pop()
            elif pivot%2 == 0:
                arr.popleft()
    
    if answer == 'error':
        print(answer)
    else:
        if func.count('R')%2 == 1:
            arr.reverse()
        answer = '['+','.join(arr)+']'
        print(answer)