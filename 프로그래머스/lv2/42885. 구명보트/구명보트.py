def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    while i < len(people):
        if people[i] + people[-1] <= limit:
            answer += 1
            i += 1
            people.pop()
        else:
            answer += 1
            people.pop()
            
    return answer