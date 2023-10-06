import math

def solution(n,a,b):
    answer = 0
    big = max(a, b); small = min(a, b)
    k = math.log2(n)
    mid = n / 2; start = 0; end = n
    while start <= end:
        if small <= mid and mid < big:
            answer += k
            break
        elif big <= mid:
            end = mid
            mid = (start + end) / 2
            k -= 1
        elif mid < small:
            start = mid
            mid = (start + end) / 2
            k -= 1

    return answer