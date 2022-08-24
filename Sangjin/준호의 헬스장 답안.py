N = int(input())
b1 = []
for i in range(N):
    c1 = input()
    c2 = c1.split()
    c2[4] = int(c2[4].strip('일'))
    c2[6] = int(c2[6].strip('시'))
    c2[7] = int(c2[7].strip('분')) #한글 제거
    if c2[6] == 12: #오전/오후를 같은 시간대로 정리
        if c2[5] == '오후':
            () #오후12시는 12시
        else:
            c2[6] = 0 #오전12시는 0시
    elif c2[5] == '오후':
        c2[6] = 12 + c2[6] #오전/오후를 같은 시간대로 정리
    c2[7] = c2[6]*60 + c2[7] #모든 시간대를 분 단위로 계산
    b1.append(c2)
# print(b1)

count = 0 #유효 출석 일수
today = 0 #시간 계산하는 날
in_time = 0 #들어온 시간
cal_time = 0 #머무른 시간 합계
plus_time = 0 #여러번 퇴장하는 경우 사용

if_in = 0 #입장한 상태에서는 1로 표시

for i in range(N):
    if today != b1[i][4]: #새 날짜가 시작
        if cal_time >= 30: #지난 날짜에 헬스장 머무른 시간 집계
            count += 1
        cal_time = 0 #저장된 시간 리셋
        today = b1[i][4]
        in_time = b1[i][7]
        if_in = 1
    else: #기존 날짜가 반복
        if b1[i][0] == '입장' and if_in == 1 : #연달아 찍힌 입장은 무시
            ()
        elif b1[i][0] == '입장' and if_in == 0 : #같은날 퇴장 후 재방문
            in_time = b1[i][7]
            if_in = 1
        elif b1[i][0] == '퇴장' and if_in == 1: #들어온 후 첫 퇴장
            cal_time += b1[i][7] - in_time #머무른 시간 저장
            if_in = 0
            plus_time = b1[i][7]
        elif b1[i][0] == '퇴장' and if_in == 0: #연달아 퇴장
            cal_time += b1[i][7] - plus_time #머무른 시간 저장
            
        if i == N-1:
            if cal_time >= 30: #오늘 날짜에 헬스장 머무른 시간 집계
                count += 1
            print(count)
    # print("i=",i, ", count= ",count,", cal_time= ",cal_time)
    # print("today= ",today, ", in_time= ", in_time)