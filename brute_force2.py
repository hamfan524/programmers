import math
from itertools import permutations

def is_num(num):

    if num == 0 or num == 1:
        return False
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True

def solution(numbers):

    answer = []

    for i in range(1, len(numbers) + 1):
        arr = list(permutations(numbers, i))
        for j in range(len(arr)):
            num = int("".join(map(str, arr[j])))
            if is_num(num):
                answer.append(num)

    answer = list(set(answer))

    return len(answer)


numbers = "002"
print(solution(numbers))