### 자릿수 더하기 ###
def solution(N) :
    NN=list(str(N))
    ans=0
    for i in NN :
        ans+=int(i)
    return ans
