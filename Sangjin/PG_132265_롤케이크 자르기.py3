from collections import Counter

#▤Counter 사용

def solution(topping):
    answer = 0
    bro1 = Counter(topping)
    bro2 = Counter([])
    for i in range(len(topping)):
        bro1[topping[i]] -= 1
        bro2[topping[i]] += 1

        #카운터에서는 개수가 0이어도 len에 집계되므로, 이를 지워준다.
        if bro1[topping[i]] == 0:
            del bro1[topping[i]]

        if len(bro1)==len(bro2):
            #print(bro1)
            answer += 1
    return answer