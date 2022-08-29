# 준호의 키보드

def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)
    return answer

s = input()
s = list(s)
print(''.join(solution(s)))