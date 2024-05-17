import heapq

def solution(n, works):
    answer = 0
    
    if sum(works) <= n:
        answer = 0
        
    else:
        work = [-i for i in works]
        heapq.heapify(work)
        
        while n > 0:
            hard = heapq.heappop(work)
            hard += 1
            n -= 1
            heapq.heappush(work, hard)
        
        for w in work:
            answer += w**2
        
    return answer