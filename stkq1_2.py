def solution(progresses, speeds):
    q = []
    for p, s in zip(progresses, speeds):
        if len(q) == 0 or q[-1][0] < -((p - 100)//s):
            q.append([-((p-100)//s), 1])
        else:
            q[-1][1] += 1
    return [answer[1] for answer in q]
    
"""
progresses = [99, 99, 99]
speeds = [1, 1, 1]
print(solution(progresses, speeds))
"""