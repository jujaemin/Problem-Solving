def solution(routes):
    answer = 1
    routes.sort()
    camera = routes[0]
    for i in range(1, len(routes)):
        if routes[i][0] <= camera[1]:
            camera = [routes[i][0], min(routes[i][1], camera[1])]
        else:
            camera = routes[i]
            answer += 1
    return answer