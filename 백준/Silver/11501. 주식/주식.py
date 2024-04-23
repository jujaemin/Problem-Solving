import sys

T = int(sys.stdin.readline())

for _ in range(T):
    total = 0
    N = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))
    prices.reverse()
    cur = prices[0]

    for i in prices:
        if cur > i:
            total += (cur-i)
        else:
            cur = i
    print(total)