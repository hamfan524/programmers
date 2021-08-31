def dfs(graph, n, path, now):
    path.append(now)

    if len(path) == n + 1:
        return True
    
    if now not in graph:
        path.pop()
        return False
    
    for _ in range(len(graph[now])):
        next = graph[now][-1]
        graph[now].pop()

        if dfs(graph, n, path, next):
            return True
        
        graph[now].insert(0, next)
    
    path.pop()
    return False

def solution(tickets):
    answer = []
    routes = {}
    for start, end in tickets:
        routes[start] = routes.get(start, []) + [end]

    for i in routes.keys():
        routes[i].sort(reverse = True)

    path = []
    if dfs(routes, len(tickets), path, "ICN"):
        answer = path

    return answer

"""
tickets = [["ICN", "ATL"], ["ICN", "SFO"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))
"""