def solution(id_list, report, k):
    answer = []
    ban = []
    banned = []

    for i in range(len(id_list)):
        answer.append(0)
    rpt = [i.split(' ') for i in list(set(report))]

    for use in rpt:
        ban.append(use[1])

    for user in id_list:
        if ban.count(user) >= k:
            banned.append(user)

    for rp in rpt:
        if rp[1] in banned:
            answer[id_list.index(rp[0])] += 1

    return answer