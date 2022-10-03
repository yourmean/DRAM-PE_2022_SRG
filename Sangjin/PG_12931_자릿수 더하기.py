def solution(n) :
    answer = 0
    n = list(map(int, str(n)))
    for _ in range(len(n)):
        answer += n[_]

    return answer