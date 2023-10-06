def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    answer = 0
    for i in range(len(A)):
        for j in range(len(B)):
            answer += (A[0] * B[0])
            del A[0]
            del B[0]
    return answer