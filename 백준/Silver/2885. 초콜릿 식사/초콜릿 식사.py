import sys

K = int(sys.stdin.readline())
bin_K = bin(K)[:1:-1]
binary = [2 ** k for k in range(28)]
cnt = len(str(int(bin_K)))
i = 1
while i < K:
    i *= 2

if K in binary:
    print(i, 0)
else:
    print(i, cnt)