import heapq
def solution(A, B):
    point = 0
    heapq.heapify(A)
    heapq.heapify(B)
    
    while A and B:
        a_v = heapq.heappop(A)
        b_v = heapq.heappop(B)

        if a_v < b_v:
            point += 1
        
        else:
            heapq.heappush(A, a_v)
        
    return point