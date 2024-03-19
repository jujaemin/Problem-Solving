import sys

N = int(sys.stdin.readline())
times = list(map(int,sys.stdin.readline().split()))
total = 0

times.sort()

for i, time in enumerate(times):
    total += time * (N-i)

print(total)