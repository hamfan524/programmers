def solution(N, number):
    dp = [0, [N]]
    if N == number:
        return 1

    for i in range(2, 9):
        lst = [int(str(N) * i)]
        
        for i_half in range(1, i // 2 + 1):
            for x in dp[i_half]:
                for y in dp[i - i_half]:
                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)
                    if y != 0:
                        lst.append(x / y)
                    if x != 0:
                        lst.append(y / x)
            if number in lst:
                return i
            dp.append(lst)
        
    return -1

"""
N = 5
number = 12
print(solution(N, number))
"""