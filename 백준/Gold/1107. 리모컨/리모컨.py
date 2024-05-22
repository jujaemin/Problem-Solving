import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
broken = list(map(int, sys.stdin.readline().split()))
usable = set()
p, least = 999999, 999999

for i in range(10):
    if i not in broken:
        usable.add(i)

if N == 100:
    least = 0
elif  not usable:
    least = abs(N-100)
else:
    while p >= 0:
        temp = set(list(map(int,str(p))))
        if temp.issubset(usable):
            least = min(abs(len(str(p)))+abs(N-p), abs(N-100), least)
        p -= 1

print(least)