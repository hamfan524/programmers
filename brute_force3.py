def solution(brown, yellow):
    num = brown + yellow
    for i in range(num, 2, -1):
        if num % i == 0:
            a = num // i
            if yellow == (i - 2) * (a - 2):
                return [i, a]

brown = 10
yellow = 2

print(solution(brown, yellow))