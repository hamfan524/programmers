def solution(priorities, location):
    answer = 0

    q = [(v, i) for i, v in enumerate(priorities)]

    while len(q):

        a = q.pop(0)

        if q and max(q)[0] > a[0]:
            q.append(a)
        else:
            answer += 1
            if a[1] == location:
                break

    return answer


priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))