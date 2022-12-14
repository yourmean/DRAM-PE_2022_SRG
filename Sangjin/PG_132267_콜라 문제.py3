def solution(a, b, n):
    answer = 0
    
    while n >= a:
        n = n -a +b
        answer += b
    
    return answer