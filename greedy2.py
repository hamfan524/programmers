def solution(name):
    answer = 0
    num = 0

    for i in name:
        if i != "A":
            num += 1
    if not num:
        return answer
    
    for i in range(len(name)):
        if ord(name[i]) < 78:
            answer += ord(name[i]) - 65
        else:
            answer += 91 - ord(name[i])

    name = list(name)

    if name[0] != "A":
        num -= 1
        name[0] = "A" 
    
    pos = 0

    for _ in range(num):
        for i in range(1, len(name)):
            r = (pos + i) % len(name)
            l = (pos - i) % len(name)

            if name[r] != "A":
                answer += i
                pos = r
                name[pos] = "A"
                break

            if name[l] != "A":
                answer += i
                pos = l
                name[pos] = "A"
                break

    return answer
"""
name = "JEROEN"
print(solution(name))
"""