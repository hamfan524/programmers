from collections import Counter

def solution(participant, completion):    
    answer = list(Counter(participant) - Counter(completion))
    return answer[0]


"""
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))
"""