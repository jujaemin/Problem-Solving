import sys

N = list(map(int, sys.stdin.readline().rstrip()))
answer = ''

if (0 not in N) or sum(N)%3 != 0:
    print(-1)

else:
    N.sort(reverse=True)
    for i in N:
        answer += str(i)
    print(int(answer))