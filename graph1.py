from collections import deque

def bfs(start, graph, visited):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        n = q.popleft()
        for g in graph[n]:
            if visited[g] == 0:
                q.append(g)
                visited[g] = visited[n] + 1

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)

    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    bfs(1, graph, visited)

    max_edge = max(visited)
    for i in visited:
        if i == max_edge:
            answer += 1

    return answer

"""
n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))
"""