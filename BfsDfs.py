def solution(numbers, target):  #bfs
    from collections import deque
    answer = 0
    q = deque()
    q.append([numbers[0], 0])
    q.append([-1 * numbers[0], 0])
    while q:
        temp, idx = q.popleft()
        idx += 1
        if idx < len(numbers):
            q.append([temp + numbers[idx], idx])
            q.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

def solution2(numbers, target):  #dfs
    answer2 = 0
    def dfs(idx, result):
        if idx == len(numbers):
            if result == target:
                nonlocal answer2
                answer2 += 1
            return
        else:
            dfs(idx+1, result + numbers[idx])
            dfs(idx-1, result - numbers[idx])
    dfs(0, 0)
    return answer2 

numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers, target))
print(solution2(numbers, target))