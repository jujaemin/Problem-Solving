import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    particiants = []
    cnt = 0

    for _ in range(N):
        document, interview = map(int, sys.stdin.readline().split())
        particiants.append([document, interview])
    
    particiants.sort(key = lambda x: x[0])
    temp = particiants[0][1]

    for part in particiants:
        if part[1] > temp:
            cnt += 1
        elif part[1] < temp:
            temp = part[1]
    
    print(N-cnt)
