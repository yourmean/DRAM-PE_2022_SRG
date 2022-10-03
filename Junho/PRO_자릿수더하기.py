def solution(n):
    s = str(n)
    answer = 0
    for j in s:
        answer += int(j)
    return answer
