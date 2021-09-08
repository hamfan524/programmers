def solution(m, n, puddles):
    dp = [list(1 for _ in range(m)) for _ in range(n)]
    
    for p in puddles:
        [x, y] = p
        dp[y-1][x-1] = 0
        if x == 1:
            for i in range(y-1, n):
                dp[i][x-1] = 0
        if y == 1:
            for i in range(x-1, m):
                dp[y-1][i] = 0
    
    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] != 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[n-1][m-1] % 1000000007

"""
m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))
"""