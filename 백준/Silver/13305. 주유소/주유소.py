import sys

N = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
cur_cost = cost[0]
total = 0

for i in range(N-1):
    if cost[i] <= cur_cost:
        cur_cost = cost[i]
    total += cur_cost*distance[i]

print(total)