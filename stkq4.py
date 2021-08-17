def solution(prices):
    from collections import deque
    prices = deque(prices)
    answer = []
    while prices:
        time = 0
        price = prices.popleft()
        for i in prices:
            time += 1
            if price > i: 
                break
        answer.append(time)
   
    return answer

"""
prices = [1, 2, 3, 2, 3]

print(solution(prices))
"""