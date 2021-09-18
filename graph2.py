from collections import defaultdict

def solution(n, results):
    answer = 0
    wins, loses = defaultdict(set), defaultdict(set)

    for r in results:
        wins[r[0]].add(r[1])
        loses[r[1]].add(r[0])

    for i in range(1, n+1):
        for winner in loses[i]:
            wins[winner].update(wins[i])
        for loser in wins[i]:
            loses[loser].update(loses[i])

    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n-1:
            answer += 1

    return answer

"""
n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))
"""