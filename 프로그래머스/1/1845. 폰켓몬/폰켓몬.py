def solution(nums):
    answer = 0
    d = {}
    N = len(nums)//2
    
    for num in nums:
        d[num] = d.get(num,0)+1

    if N < len(d):
        answer = N
    else:
        answer = len(d)
        
    return answer