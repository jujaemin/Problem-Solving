import sys

N, M = map(int, sys.stdin.readline().split())
get_nums = list(map(int, sys.stdin.readline().split()))
nums = [0]
nums.extend(get_nums)
sum_list = []
result = 0
for num in nums:
    result += num
    sum_list.append(result)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    answer = sum_list[j] - sum_list[i-1]
    print(answer)