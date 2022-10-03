def solution(id_list, report, k):
    answer = []
    
    
    #각 아이디별 신고한 사람 딕셔너리 저장하는 곳
    dic_id = {id:[] for id in id_list}
    #정지된 ID를 신고한 사람 리스트
    report_success_list = []
    
    for i in range(len(report)):
        #신고자(from)와 신고당한 사람(to) 각각 표시
        r_from, r_to = report[i].split() 
        dic_id[r_to].append(r_from)
    
    for i in range(len(id_list)):
        if len(set(dic_id[id_list[i]])) >= k:
            #신고에 성공한 사람들은 따로 저장(list의 내용물을 추가하는 것이므로 append 대신 extend 사용)
            report_success_list.extend(list(set(dic_id[id_list[i]])))
    
    for i in range(len(id_list)):
        answer.append(report_success_list.count(id_list[i]))
    
    return answer