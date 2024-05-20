import sys

N = sys.stdin.readline().rstrip()
checked = [0]*10

for i in N:
    if i == '6' or i == '9':
        if checked[6] <= checked[9]:
            checked[6] += 1
        else:
            checked[9] += 1
    else:
        checked[int(i)] += 1

print(max(checked))