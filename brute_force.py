def solution(answers):
    answer = []
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]


    for i in range(len(answers)):
        if student1[i % 5] == answers[i]:
            score[0] += 1
        if student2[i % 8] == answers[i]:
            score[1] += 1
        if student3[i % 10] == answers[i]:
            score[2] += 1

    max_ = max(score)

    for i in range(len(score)):
        if score[i] == max_:
            answer.append(i + 1)

    return answer

answers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(solution(answers))