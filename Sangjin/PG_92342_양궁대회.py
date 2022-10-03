#조합형 이터레이터
from itertools import combinations_with_replacement as cwr

def solution(n, info): 
    
    answer = [-1]
    
    #0~10 사이 수를 중복 포함 n개 뽑는다, 예: (0,3,5,7,10)
    #라이언이 쏜 과녁을 의미
    iter_com = list(cwr(range(0, 11), n))
    #cwr의 결과창
    #(0,0,0,0,0), (0,0,0,0,1), ..., (10, 10, 10, 10, 10)
    #라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주어야한다.
    #info의 i번째 원소는 과녁의 10 - i 점을 맞힌 화살 개수
    #낮은 점수(i가 높은 수)를 먼저 채우면서 candidates가 돌아야 한다.

    max_gap = -1

    for i_c in iter_com:
        lion_info = [0] * 11

        #각자 점수는 0에서 출발
        apch_point, lion_point = 0, 0

        for num in i_c:  
            #info의 i번째 원소는 과녁의 10 - i 점을 맞힌 화살 개수
            #[10, 9, 8, ..., 1, 0]
            lion_info[10 - num] += 1

        #인덱스와 함께 값을 추출
        #enumerate와 zip을 동시에 사용
        for num, (apch, lion) in enumerate(zip(info, lion_info)):
            #둘 다 안 쏜 경우
            if apch == lion == 0:
                continue
            #어피치가 이긴 경우
            elif apch >= lion:
                apch_point += (10 - num)
            #라이언이 이긴 경우
            else:
                lion_point += (10 - num)

        if lion_point > apch_point:
            gap = lion_point - apch_point
            if gap > max_gap: #등호는 들어가면 안된다
                max_gap = gap
                #라이언이 이길 수 있는 경우에는 답이 [-1]에서 바뀌게 된다.
                answer = lion_info

    return answer