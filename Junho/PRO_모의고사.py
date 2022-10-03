def solution(answers):
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    la1 = len(a1)
    la2 = len(a2)
    la3 = len(a3)
    
    c1, c2, c3 = 0, 0, 0
    result = []
    
    for i in range(len(answers)):
        if a1[i % la1] == answers[i]:
            c1 += 1
        if a2[i % la2] == answers[i]:
            c2 += 1
        if a3[i % la3] == answers[i]:
            c3 += 1
    


    aa = max(c1, c2, c3)
    
    if aa == c1:
        result.append(1)
    if aa == c2:
        result.append(2)
    if aa == c3:
        result.append(3)
        
    return result
