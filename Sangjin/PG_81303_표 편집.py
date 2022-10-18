def solution(n, k, cmd):
    dic_1 = list(range(n))
    dic_2 = [["O",i-1,i+1] for i in range(n)]
    dic_2[0][1] = "끝"
    dic_2[n-1][2] = "끝"
    dic = dict(zip(dic_1, dic_2))
    #dic의 구성: [del 여부 O/X, 앞번호, 뒷번호]
    
    #현재 선택된 칸
    loc = k

    #지운 칸 저장하는 곳
    stack = []
    
    for i in range(len(cmd)):
        if cmd[i] == "Z":
            #가장 최근에 지운 것 불러오기
            left, right, recent = stack.pop(-1)
            dic[recent][0] = "O"

            #앞뒤 좌표 입력
            if dic[recent][1] == "끝":
                dic[dic[recent][2]][1] = recent
            elif dic[recent][2] == "끝":
                dic[dic[recent][1]][2] = recent
            else:
                dic[dic[recent][1]][2] = recent
                dic[dic[recent][2]][1] = recent
                
        elif cmd[i] == "C":
            #뭐 지웠는지 저장
            left, right = dic[loc][1], dic[loc][2]
            stack.append([left, right, loc])
            #현재 위치 삭제
            dic[loc][0] = "X"
            
            #앞뒤 좌표와 선택된 행 변경
            if dic[loc][1] != "끝":
                dic[dic[loc][1]][2] = dic[loc][2]
            if dic[loc][2] != "끝":
                dic[dic[loc][2]][1] = dic[loc][1]
                loc = dic[loc][2]
            else:
                loc = dic[loc][1]
        else:
            cmd_1, cmd_2 = cmd[i].split()
            if cmd_1 == "D":
                for _ in range(int(cmd_2)):
                    loc = dic[loc][2]
            else:
                for _ in range(int(cmd_2)):
                    loc = dic[loc][1]
        # print(dic)

    pre_answer = []

    for value in dic.values():
        pre_answer.append(value[0])  
    answer = "".join(pre_answer)
    return answer