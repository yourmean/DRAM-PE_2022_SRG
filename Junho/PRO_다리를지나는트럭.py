def solution(bridge_length, weight, truck_weights):
    time = 0
    dari = [0] * bridge_length
    
    while dari:
        dari.pop(0)
        time += 1
        if truck_weights:
            if sum(dari) + truck_weights[0] <= weight:
                dari.append(truck_weights.pop(0))
            else:
                dari.append(0)
    
    return time
