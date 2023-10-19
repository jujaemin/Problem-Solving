def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    answer = len(d)
    return answer