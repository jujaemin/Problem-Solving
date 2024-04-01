import sys

N = int(sys.stdin.readline())

cards = list(map(int, sys.stdin.readline().split()))
price = [0]
price.extend(cards)

for i in range(2, N+1):
    for j in range(1,i+1):
        price[i] = min(price[i], price[j]+cards[i-j-1])

print(price[N])