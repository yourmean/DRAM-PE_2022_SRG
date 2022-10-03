def solution(bridge_length, weight, truck_weights):
    answer = 0


    total_time = 0 #전체 걸리는 시간
    fin = 0 #도착한 차 수
    truck_on_bridge = [] #다리를 건너는 트럭들
    location_on_bridge = [] #트럭들의 위치
    total_num = len(truck_weights) #전체 트럭 수

    while True:
        total_time += 1
        #달리고 있던 트럭들 한 칸씩 앞으로 이동
        location_on_bridge = [i+1 for i in location_on_bridge]

        #도착지에 간 트럭 반영
        if len(location_on_bridge) != 0:
            if location_on_bridge[0] >= bridge_length:
                location_on_bridge.pop(0) #달리는 차에서 삭제
                truck_on_bridge.pop(0) #달리는 차에서 삭제
                fin += 1
                if fin == total_num:
                    break #전부 다 도착했으면 break

        #트럭이 한 대 출발
        if len(truck_weights) != 0:
            if sum(truck_on_bridge) + truck_weights[0] <= weight:
                truck_on_bridge.append(truck_weights.pop(0))
                location_on_bridge.append(0)

    answer = total_time
    return answer
