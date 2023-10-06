def solution(n, words):
    answer = []
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
                answer = [(i%n)+1, (i//n)+1]
                break
        else:
            answer = [0,0]   

    return answer