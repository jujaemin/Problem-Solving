import sys

N = int(sys.stdin.readline())
triangle= []

for i in range(N) :
    triangle.append(list(map(int,sys.stdin.readline().split())))
for i in range(len(triangle)-2,-1,-1):
        for j in range(i+1):
            triangle[i][j] = max(triangle[i][j]+triangle[i+1][j], triangle[i][j]+triangle[i+1][j+1])
            
print(triangle[0][0])