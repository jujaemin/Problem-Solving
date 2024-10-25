from itertools import permutations

def prime(n):
    for j in range(2, int(n ** (0.5))+1):
        if n % j == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    nums = []
    for i in range(1, len(numbers)+1):
        nums.append(list(map(''.join,permutations(numbers,i))))
    nums = sum(nums,[])
    nums = list(set(map(int, nums)))
    for num in nums:
        if num >= 2:
            if prime(num) == True:
                answer += 1
    return answer