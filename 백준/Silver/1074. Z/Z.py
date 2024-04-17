import sys

N,r,c = map(int, sys.stdin.readline().split())
result = 0

while N > 0:
    N -= 1

    if (r < 2 ** N) and (c < 2 ** N):
        continue

    if (r < 2 ** N) and (c >= 2 ** N):
        c -= 2 ** N
        result += 2 ** (2*N)

    if (r >= 2 ** N) and (c < 2 ** N):
        r -= 2 ** N
        result += 2 * 2 ** (2*N)

    if (r >= 2 ** N) and (c >= 2 ** N):
        r -= 2 ** N
        c -= 2 ** N
        result += 3 * 2 ** (2*N)

print(result)