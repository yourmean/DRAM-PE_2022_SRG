def solution(tp):
    r1, r2 = set(), set()
    rlen1, rlen2 = [], []
    
    for s in tp:
        r1.add(s)
        rlen1.append(len(r1))
    for s in tp[::-1]:
        r2.add(s)
        rlen2.append(len(r2))
        
    rlen2 = rlen2[::-1]
    
    answer = 0
    for k in range(len(rlen1)-1):
        if rlen1[k] == rlen2[k+1]:
            answer += 1
    
    return answer
