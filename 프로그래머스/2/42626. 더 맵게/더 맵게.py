import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2:
        min_ = heapq.heappop(scoville)
        if min_ >= K:
            return answer
        else:
            min_2 = heapq.heappop(scoville) 
            heapq.heappush(scoville, min_ + 2 * min_2)
            answer += 1
    if scoville[0] >= K:
        return answer
    else:
        return -1