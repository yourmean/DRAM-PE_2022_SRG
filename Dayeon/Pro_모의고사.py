def solution(answers) :
    n1=[1,2,3,4,5]
    n2=[2,1,2,3,2,4,2,5]
    n3=[3,3,1,1,2,2,4,4,5,5]
    r1=0 ; r2=0 ; r3=0
    for i in range(0,len(answers)):
        if n1[i%len(n1)]==answers[i]: r1+=1
        if n2[i%len(n2)]==answers[i]: r2+=1
        if n3[i%len(n3)]==answers[i]: r3+=1
    M=max(r1,r2,r3)
    ret=[]
    if r1==M : ret.append(1)
    if r2==M : ret.append(2)
    if r3==M : ret.append(3)
    return ret