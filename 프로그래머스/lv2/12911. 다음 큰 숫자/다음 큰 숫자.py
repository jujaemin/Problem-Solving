def solution(n):
    bin_n = bin(n)[2: ]
    con = True
    answer = 0
    while con:
        n += 1
        bi = bin(n)[2: ]
        if bin_n.count('1') == bi.count('1'):
            answer = n
            con = False
    return answer