import heapq

def solution(operations):
    answer = []
    heap = []
    for op in operations:
        x, value = op.split()
        value = int(value)
        
        if x =='I':
            heapq.heappush(heap, value)
        
        elif x == 'D' and value == 1:
            if heap:
                max_val = max(heap)
                heap.remove(max_val)
        
        else:
            if heap:
                heapq.heappop(heap)
                
    if not heap:
        answer = [0,0]
    
    else:
        max_res = max(heap)
        min_res = heap[0]
    
        answer.append(max_res)
        answer.append(min_res)
    
    return answer