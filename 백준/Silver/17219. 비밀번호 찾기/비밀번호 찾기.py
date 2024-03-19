import sys

N, M = map(int,sys.stdin.readline().split())
dict = {}

for _ in range(N):
    site, password = sys.stdin.readline().split()
    dict[site] = password

for _ in range(M):
    find = sys.stdin.readline().strip()
    print(dict[find])