import sys

N = int(sys.stdin.readline())
nums= list(map(int, sys.stdin.readline().split()))

sorted_numbers = list(sorted(set(nums)))
result = {value:index for index, value in enumerate(sorted_numbers)}

for num in nums:
    print(result[num], end= ' ')