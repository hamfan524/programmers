def solution(progresses, speeds):
    answer = []
    q = []
    i = 0
    day = 0
    while i <= len(progresses) - 1:
        day += 1
        progresses[i] += speeds[i]
        if progresses[i] >= 100:
            q.append(day)
            i += 1
            day = 0

    day = 1
    a = q.pop(0)
    answer.append(day)
    while q:
        if a >= q[0]:
            answer[-1] += 1
            q.pop(0)
        else:
            a = q.pop(0)
            answer.append(day)
  
    return answer
"""
progresses = [99, 99, 99]
speeds = [1, 1, 1]
print(solution(progresses, speeds))
"""