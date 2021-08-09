def solution(number, k):
    stack = []
    for i in number:
        while stack and stack[-1] < i and k > 0:
            k -= 1
            stack.pop()
        stack.append(i)

    answer = "".join(stack[:len(stack) - k])
    return answer
"""
number = "4177252841"
k = 4
print(solution(number, k))
"""