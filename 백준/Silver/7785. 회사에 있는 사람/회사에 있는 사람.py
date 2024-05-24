import sys

n = int(sys.stdin.readline())
people = {}
result = []

for _ in range(n):
    name, record = sys.stdin.readline().split()
    people[name] = record

for i in people.keys():
    if people[i] == 'enter':
        result.append(i)

result.sort(reverse=True)

for j in result:
    print(j)