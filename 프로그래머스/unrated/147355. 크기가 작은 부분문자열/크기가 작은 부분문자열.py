def solution(t, p):
    answer = 0
    tl, pl = len(t), len(p)
    comp = []
    for i in range(tl-pl+1):
        com = ""
        for j in range(pl):
            com += t[i+j]
        comp.append(com)
    for k in comp:
        if int(k) <= int(p):
            answer += 1
    return answer