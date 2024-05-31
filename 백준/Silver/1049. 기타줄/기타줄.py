import sys

N, M = map(int, sys.stdin.readline().split())
strings = []
price = 0

for _ in range(M):
    strings.append(list(map(int, sys.stdin.readline().split())))

six_in_one = sorted(strings, key = lambda x: x[0])
one = sorted(strings, key = lambda x: x[1])

while N > 0:
    if one[0][1] * 6 < six_in_one[0][0]:
        price += one[0][1] * N
        break
    else:
        if N >= 6:
            price += six_in_one[0][0] * (N // 6)
            N %= 6
        else:
            price += min(six_in_one[0][0], one[0][1] * N)
            break

print(price)