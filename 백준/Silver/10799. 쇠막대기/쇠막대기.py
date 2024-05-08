import sys

sticks = list(sys.stdin.readline().rstrip())
cnt = 0
stack = []

for i in range(len(sticks)):
    if sticks[i] == '(':
        stack.append('(')
    
    else:
        if sticks[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)