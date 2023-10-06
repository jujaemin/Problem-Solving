def solution(s):
    cnt0, cnt = 0, 0
    while len(s) != 1:
        c0 = s.count('0')
        cnt0 += c0
        x = str(bin(len(s.replace('0', '')))[2: ])
        s = x
        cnt += 1
    return [cnt, cnt0]