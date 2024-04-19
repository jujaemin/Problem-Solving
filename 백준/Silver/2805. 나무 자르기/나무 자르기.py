import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
max_h, min_h = max(trees), 1
result = 0

while max_h >= min_h:
    mid_h = (max_h+min_h)//2
    rest = []
    for tree in trees:
        if tree > mid_h:
            rest.append((tree-mid_h))
    sum_trees = sum(rest)
    if sum_trees >= M:
        result = mid_h
        min_h = mid_h+1
    elif sum_trees < M:
        max_h = mid_h-1

print(result)