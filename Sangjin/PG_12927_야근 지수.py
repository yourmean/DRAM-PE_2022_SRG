import heapq
#heapq.heapify 사용: 최소값을 배열의 맨 앞에 유지시켜줌

'''
works를 heapq 배열로 만들어주되, 모든 값에 '-'를 붙임.
heapq는 최소값이 우선이기 때문에,
'-'를 붙이게 되면 최솟값이 아닌 최대값 기준으로 정렬한 것과 같은 효과를 볼 수 있음.
그냥 heapq 사용할 경우 : [1, 7, 8, 9]
'-' 붙여서 heapq 사용할 경우 : [-9, -8, -7, -1]
'''    

def solution(n, works):
    #야근을 안해도 되는 상황이면 0을 출력한다.
    if sum(works) <= n:
        return 0
    
    answer = 0
    
    #'-'를 붙여서 heapq 정렬(오름차순)
    works = [-i for i in works]
    heapq.heapify(works)
    
    while n > 0:
        max_val = heapq.heappop(works) #제일 작은 수(절댓값이 가장 큰 수)를 제거한다.
        heapq.heappush(works, max_val+1) #push하면 알아서 정렬된다.
        n -= 1
    
    #절댓값이 골고루 작아진 값을 대상으로 야근 지수를 계산한다.
    for i in works:
        answer += i ** 2
    return answer


#참고용: 시간초과되었던 답안 형태(itertools의 product 사용)
'''
from itertools import product

#야근지수를 계산해주는 함수
def calc(remain_works):
    calc_num = 0
    for i in range(len(remain_works)):
        calc_num += remain_works[i] * remain_works[i]
    return calc_num

#남은 일의 합계를 계산해주는 함수
def sum_calc(remain_works):
    calc_num = 0
    for i in range(len(remain_works)):
        calc_num += remain_works[i]
    return calc_num
  
if sum_calc(works) <= n:
    print(0)

cand_num = calc(works) #일을 하기 전 야근 지수 값을 넣어둔다.
cand_works = []

for case in product(range(n+1), repeat=len(works)):
    #len(works)=3, n=6인 경우 product 결과물
    #(0, 0, 0) (0, 0, 1) (0, 0, 2), ... (5, 5, 5)
    
    #합계가 n과 같아야한다.
    print("흠흠", case)  
    if sum_calc(case) == n:
        #각각 남은 일만큼 주어졌는지 확인한다.
        remain_check = True
        print("흠", case)
        for i in range(len(works)):
            if case[i] > works[i]:
                remain_check = False
                break
        #product에서 배정 결과가 제대로 된 경우만 가지고 진행한다.
        print(case)
        tem_works = []
        if remain_check:
            print("통과", case)
            for i in range(len(case)):
                tem_works.append(works[i] - case[i])
        
        #야근지수가 더 적은 경우를 최선의 경우로 본다.
        tem_num = calc(tem_works)
        print(cand_num, tem_num)
        if remain_check and cand_num > tem_num:
            cand_num = tem_num
            cand_works = tem_works
            print(cand_works)
print(cand_works)
'''

