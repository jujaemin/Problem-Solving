import sys
from collections import deque

N = int(sys.stdin.readline())
bin_N = bin(N)

print(bin_N.count('1'))