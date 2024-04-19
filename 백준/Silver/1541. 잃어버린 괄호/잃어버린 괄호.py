import sys

problem = sys.stdin.readline().rstrip()
result = []

nums = problem.split('-')

for i in nums:
    sum = 0
    i = i.split('+')
    for j in i:
        sum += int(j)
    result.append(sum)

answer = result[0]

for k in range(1, len(result)):
    answer -= result[k]

print(answer)