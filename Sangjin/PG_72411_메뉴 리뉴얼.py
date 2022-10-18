from itertools import combinations
#각 원소가 몇 번씩 나오는지가 저장된 객체를 얻게 된다.
from collections import Counter
#사용예
# 입력: Counter("hello world")
# Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

def solution(orders, course):
    answer = []
    
    for c_i in course:
        tem = []
        for o_i in orders:
            cbnt = combinations(sorted(o_i), c_i)
            tem += cbnt
        #tem 출력 결과(c_i = 2인 경우)
        #[('A', 'B'), ('A', 'C'), ... , ('D', 'E'), ('X', 'Y'), ... ,('C', 'D')] 
        counter = Counter(tem)
        #counter 출력 결과
        #Counter({('A', 'D'): 3, ('C', 'D'): 3, ... , ('C', 'E'): 1})
        
        #조합이 하나 이상 있어야 함 & 중복된 개수가 1보다 커야 함
        if len(counter) != 0 and max(counter.values()) != 1:
            #max(counter.values) : 가장 많이 함께 주문한 것을 선택
            #''.join(f) : 분리된 글자들을 한데 모은다 ('A', 'D') -> ('AD')
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)
    return answer