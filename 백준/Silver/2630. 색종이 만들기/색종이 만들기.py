import sys

N = int(sys.stdin.readline())

paper = []
count_whilte = 0
count_blue = 0

for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))


def solution(x, y, n):
    global count_blue, count_whilte      
    check = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != check:
                solution(x, y, n//2)
                solution(x+n//2, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y+n//2, n//2)
                return
           
    if check == 0:
          count_whilte += 1
    else:
          count_blue += 1

solution(0,0,N)

print(count_whilte)
print(count_blue)