# 생각보다 시간 많이 걸림 -> pop(0) 때문인듯

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    total_weight = 0  # 현재 다리 위 모든 트럭의 무게 합

    while truck_weights:
        total_weight -= bridge.pop(0)  # 맨 앞 트럭 빠져나가기 or 0

        # 새로운 트럭 올리기 가능한 경우 : 대기 트럭 올려서 다리에 추가& 모든 트럭의 무게 합 update
        if total_weight + truck_weights[0] <= weight:
            a = truck_weights.pop(0)
            bridge.append(a)
            total_weight += a

        # 새로운 트럭 올리기 불가능한 경우 : 0 append (for 다리 길이 유지)
        else:
            bridge.append(0)

        answer += 1

    return answer + bridge_length  # 마지막 트럭이 다리 건너는 시간 +