import heapq

def solution(operations):
    answer = []
    heap = []

    for op in operations:
        x, value = op.split()
        value = int(value)

        if x == 'I':
            heapq.heappush(heap, value)
        
        elif x == 'D' and value == 1:
            if heap:
                max_val = max(heap)
                heap.remove(max_val)
        
        else:
            if heap:
                heapq.heappop(heap)
    
    if heap:
        answer.append(max(heap))
        answer.append(heapq.heappop(heap))
    else:
        answer = [0,0]
    return answer