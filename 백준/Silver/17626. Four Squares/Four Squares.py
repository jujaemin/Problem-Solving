import sys
import math

n = int(sys.stdin.readline())
nums = [0 for _ in range(50001)]

for num in range(1, int(math.sqrt(n)+1)):
    nums[num**2] = 1

nums[2] = 2
nums[3] = 3

for i in range(1, n+1):
    temp = 4
    if nums[i] == 0:
        for j in range(1, int(math.sqrt(i))+1):
            if nums[i-j**2]+1 < temp:
                temp = nums[i-j**2]+1
        nums[i] = temp

print(nums[n])