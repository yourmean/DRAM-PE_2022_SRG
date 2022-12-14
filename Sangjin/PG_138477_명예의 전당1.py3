def solution(k, score):
    answer = []
    honor = []
    
    for i in range(len(score)):
        honor.append(score[i])
        honor.sort(reverse=True)
        if i <= k-1:
            answer.append(honor[i])
        else:
            answer.append(honor[k-1])
    
    return answer