def solution(s):
    stack = []
    for ex in s:
        if ex =='(':
            stack.append(ex)
        elif ex ==')':
            if len(stack) == 0 or stack[len(stack)-1] == ')':
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False
                
            