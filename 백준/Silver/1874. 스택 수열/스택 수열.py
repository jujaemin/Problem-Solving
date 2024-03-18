import sys
from collections import deque

n = int(sys.stdin.readline())
stacks = deque()
checkpoint = 0
result = []

for _ in range(n):
    check = int(sys.stdin.readline())    

    if not stacks or check > stacks[-1]:
        for i in range(checkpoint+1, check+1):
            stacks.append(i)
            result.append('+')
            checkpoint = check
        result.append('-')
        stacks.pop()

    elif check == stacks[-1]:
        result.append('-')
        stacks.pop()
    
    elif check < stacks[-1]:
        result.append('NO')

if 'NO' in result:
    print('NO')

else:
    for res in result:
        print(res)