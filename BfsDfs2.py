from collections import deque

def bfs(n, computers, j, visited):
    visited[j] = True
    q = deque()
    q.append(j)
    while q:
        temp = q.popleft()
        visited[temp] = True
        for i in range(n):
            if i != temp and computers[temp][i] == 1:
                if visited[i] == False:
                    q.append(i)

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:
            bfs(n, computers, i, visited)
            answer += 1
    return answer
    
"""
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n = 3

print(solution(n, computers))
"""