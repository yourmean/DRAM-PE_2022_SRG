def solution(answers):
    answer = []

    #수포자들 답안 제출 형식
    sp1 = [1,2,3,4,5]
    sp2 = [2,1,2,3,2,4,2,5]
    sp3 = [3,3,1,1,2,2,4,4,5,5]

    #수포자들 점수
    grade = [0,0,0]

    #하나씩 채점하기
    for i in range(len(answers)):
        Q = answers[i]
        if sp1[i%len(sp1)] == Q:
            grade[0] += 1
        if sp2[i%len(sp2)] == Q:
            grade[1] += 1
        if sp3[i%len(sp3)] == Q:
            grade[2] += 1

    #최고 득점자 찾기
    if grade[0] == max(grade):
        answer.append(1)
    if grade[1] == max(grade):
        answer.append(2)
    if grade[2] == max(grade):
        answer.append(3)

    return answer