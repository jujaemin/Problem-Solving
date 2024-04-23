import sys

poly = sys.stdin.readline().rstrip().split('.')
result = []

for s in poly:
    n = len(s)
    if n%2 == 1:
        result.append(-1)
    else:
        rep = ('AAAA' * (n // 4))+('B' * (n%4))+'.'
        result.append(rep)

if -1 in result:
    print(-1)
else:
    print(''.join(result)[:-1])