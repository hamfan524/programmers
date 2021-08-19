def solution(array, commands):
    answer = []
   
    for i in commands:
        a = i[0] - 1
        b = i[1]
        copy = array[a:b]
        copy.sort()
        answer.append(copy[i[2]-1])
    return answer

"""
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))
"""