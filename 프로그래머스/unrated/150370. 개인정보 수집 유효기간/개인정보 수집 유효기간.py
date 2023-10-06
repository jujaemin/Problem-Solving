def compare(date, today):
    if date[0] > today[0]:
        return True
    if date[0] == today[0] and date[1] > today[1]:
        return True
    if date[0] == today[0] and date[1] == today[1] and date[2] > today[2]:
        return True
    else:
        return False

def solution(today, terms, privacies):
    answer = []
    j = 1
    today = list(map(int,today.split(".")))
    expiration = {term[0]:int(term[2:]) for term in terms}

    for i in privacies:
        prv = i.split(' ')
        date = list(map(int, prv[0].split('.')))
        date[1] += expiration[prv[1]]

        if date[1] > 12:
            if (date[1] % 12) == 0:
                date[0] += (date[1]//12) -1
                date[1] = 12
            else:
                date[0] += (date[1]//12)
                date[1] %= 12
        
        if compare(date, today) == False:
            answer.append(j)
        j += 1

    return answer