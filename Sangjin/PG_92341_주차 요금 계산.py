import math #올림 계산용

def solution(fees, records):
    answer = []
    t_time = []

    #차량들 모임
    cars = {}

    for i in range(len(records)):
        time, car, io = records[i].split()
        #차량 목록에 추가
        if car not in cars:
            cars[car] = [] 
        #차량별로 시간 저장
        cars[car].append(time) 

    #시간이 홀수로 입력되어있으면 23:59 출차 추가 
    for i in range(len(list(cars.keys()))):
        if len(cars[list(cars.keys())[i]]) % 2 == 1:
            cars[list(cars.keys())[i]].append("23:59")

    #차량 번호가 작은 자동차부터 나오도록 정렬
    cars_list = list(cars.keys())
    cars_list.sort()

    #내부에 있던 시간 계산 -> 주차시간 계산
    for i in range(len(cars_list)):
        i_time = 0
        for j in range(len(cars[cars_list[i]])):
            if j%2 == 0: #짝수: IN (0부터 시작)
                in_time_str = cars[cars_list[i]][j]
                out_time_str = cars[cars_list[i]][j+1]

                #시간을 분 단위로 변환
                a,b = in_time_str.split(":")
                c,d = out_time_str.split(":")
                i_time += (int(c)*60 + int(d)) - (int(a)*60 + int(b))
        t_time.append(i_time)

    #주차요금 계산
    for i in range(len(t_time)):
        #기본시간 이하인 경우 기본 요금 청구
        if t_time[i] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(math.ceil((t_time[i]-fees[0])/fees[2]) * fees[3] + fees[1])

    return answer