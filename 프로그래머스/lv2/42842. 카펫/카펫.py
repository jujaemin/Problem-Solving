def solution(brown, yellow):
    answer = []
    
    divisorsList = []

    for i in range(1, int(yellow ** (1/2)) + 1):
        if (yellow % i == 0):
            divisorsList.append([i, yellow//i]) 
            if ( (i**2) != yellow) : 
                divisorsList.append([yellow // i, yellow  // i])
    
    for j in divisorsList:
        if ((j[0]+2) * 2) + (j[1] * 2) == brown:
            answer.append([j[0]+2, j[1]+2])
    
    if answer[0][0] < answer[0][1]:
        temp = answer[0][0]
        answer[0][0] = answer[0][1]
        answer[0][1] = temp
    
    answer = answer[0]
    return answer

print(solution(10, 2))