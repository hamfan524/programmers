def solution(money):
    dp = [0 for _ in range(len(money) - 1)]
    dp_ = [0 for _ in range(len(money))]

    dp[0] = money[0]
    dp[1] = max(dp[0], money[1])

    dp_[0] = 0
    dp_[1] = money[1]

    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    for i in range(2, len(money)):
        dp_[i] = max(dp_[i-1], dp_[i-2] + money[i])

    return max(dp[-1], dp_[-1])

"""
money = [1, 2, 3, 1]
print(solution(money))
"""