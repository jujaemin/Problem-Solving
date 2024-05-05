import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
result = 0

while A and B:
    min_A, max_B = 999, 0

    for i in range(len(A)):
        if A[i] < min_A:
            min_A = A[i]
        if B[i] > max_B:
            max_B = B[i]
    
    result += (min_A*max_B)
    A.remove(min_A)
    B.remove(max_B)

print(result)