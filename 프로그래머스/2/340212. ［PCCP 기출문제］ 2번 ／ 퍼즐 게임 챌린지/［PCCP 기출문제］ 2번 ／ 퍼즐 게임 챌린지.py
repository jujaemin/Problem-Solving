def solution(diffs, times, limit):
    
    def binary_search(start, end):
    
        mid = (start + end) // 2
        total = times[0]
        
        if start == end:
            return mid
    
        for i in range(1, len(times)):
            if diffs[i] > mid:
                total += ((times[i]+times[i-1])*(diffs[i]-mid))+times[i]
            
            else:
                total += times[i]
    
        if total > limit:
            start = mid+1
        
        else:
            end = mid
        
        return binary_search(start, end)
    
    start, end = min(diffs), max(diffs)
    answer = binary_search(start, end)
    
    return answer