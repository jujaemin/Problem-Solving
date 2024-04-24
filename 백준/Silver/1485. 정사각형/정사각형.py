import sys
import math

T = int(sys.stdin.readline())

for _ in range(T):
    square = []

    for _ in range(4):
        x,y = map(int, sys.stdin.readline().split())
        square.append((x,y))
    square.sort()
    
    if (math.sqrt(((square[0][0]-square[1][0])**2)+((square[0][1]-square[1][1])**2)) == math.sqrt(((square[0][0]-square[2][0])**2)+((square[0][1]-square[2][1])**2)) 
        == math.sqrt(((square[2][0]-square[3][0])**2)+((square[2][1]-square[3][1])**2)) == math.sqrt(((square[1][0]-square[3][0])**2)+((square[1][1]-square[3][1])**2))):
        if (math.sqrt(((square[0][0]-square[3][0])**2)+((square[0][1]-square[3][1])**2)) == math.sqrt(((square[1][0]-square[2][0])**2)+((square[1][1]-square[2][1])**2))) :
            print(1)
        else:
            print(0)
        
    
    else:
        print(0)