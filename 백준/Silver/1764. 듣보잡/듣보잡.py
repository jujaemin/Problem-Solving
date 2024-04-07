import sys

N, M = map(int, sys.stdin.readline().split())
dbj = {}
result = []

for _ in range(N):
    ds = sys.stdin.readline().rstrip()
    dbj[ds] = dbj.get(ds, 0) + 1

for _ in range(M):
    bs = sys.stdin.readline().rstrip()
    dbj[bs] = dbj.get(bs, 0) + 1


for key in dbj.keys():
    if dbj[key] == 2:
        result.append(key)

result.sort()

print(len(result))
for res in result:
    print(res)