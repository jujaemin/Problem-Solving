import sys

N = int(sys.stdin.readline())

apples = []
pears = []
weight = 0
apple_price = 0

for _ in range(N):
    box = list(input().split())

    if box[0] == 'A':
        apples.append(box)
    
    else:
        pears.append(box)

weight += (1000 * len(apples)) + (6000 * len(pears))

for apple in apples:
    apple_cnt = (int(apple[1]) // 12) * (int(apple[2]) // 12) * (int(apple[3]) // 12)
    weight += apple_cnt * 500
    apple_price += apple_cnt * 4000

print(weight)
print(apple_price)