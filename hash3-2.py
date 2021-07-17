from collections import Counter
from functools import reduce

def solution(clothes):
    ans = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y : x * (y + 1), ans.values(), 1) - 1
    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))