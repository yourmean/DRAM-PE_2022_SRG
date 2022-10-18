def solution(record):
    answer = []
    
    #들어가고 나간 기록
    history = []
    #아이디와 닉네임 기록
    id_nick = dict()
    
    for i in range(len(record)):
        re_sp = record[i].split(" ")
        if re_sp[0] == "Enter":
            history.append(["E", re_sp[1]])
            id_nick[re_sp[1]] = re_sp[2]
        elif re_sp[0] == "Leave":
            history.append(["L", re_sp[1]])
        elif re_sp[0] == "Change":
            id_nick[re_sp[1]] = re_sp[2]
        else:
            print("Err")
    
    #유저 아이디를 닉네임으로 바꾸기
    for i in range(len(history)):
        history[i][1] = id_nick[history[i][1]]
    
    for i in range(len(history)):
        if history[i][0] == "E":
            answer.append(history[i][1] + "님이 들어왔습니다.")
        elif history[i][0] == "L":
            answer.append(history[i][1] + "님이 나갔습니다.")
        else:
            print("ERR")
    
    return answer