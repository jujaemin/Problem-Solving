import sys

N = int(sys.stdin.readline())
drinks = list(map(int, sys.stdin.readline().split()))
max_drink = max(drinks)
print((max_drink/2)+(sum(drinks)/2))