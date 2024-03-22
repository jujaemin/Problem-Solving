def dfs(n,computers,com,visited):
    visited[com] = True
    for conn in range(n):
        if conn != com and computers[com][conn] == 1:
            if visited[conn] == False:
                dfs(n,computers,conn,visited)

def solution(n, computers):
    visited = [False] * n
    answer = 0
    for com in range(n):
        if visited[com] == False:
            dfs(n,computers,com,visited)
            answer += 1
    return answer