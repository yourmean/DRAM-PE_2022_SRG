ans1 = [1, 2, 3, 4, 5]
ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
score = [0, 0, 0]


def solution(answers):
    ans = []
    for i in range(len(answers)):
        if ans1[i % len(ans1)] == answers[i]:
            score[0] += 1
        if ans2[i % len(ans2)] == answers[i]:
            score[1] += 1
        if ans3[i % len(ans3)] == answers[i]:
            score[2] += 1

    for i in range(3):
        if score[i] == max(score):
            ans.append(i + 1)

    return ans