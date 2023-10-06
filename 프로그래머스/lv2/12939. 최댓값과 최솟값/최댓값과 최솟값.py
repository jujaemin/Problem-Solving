def solution(s):
    num_list = list(map(int, s.split()))
    return('{} {}'.format(min(num_list), max(num_list)))                