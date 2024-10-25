def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        cur = phone_book[i]
        if phone_book[i+1].startswith(phone_book[i]):
                answer = False
        
    return answer