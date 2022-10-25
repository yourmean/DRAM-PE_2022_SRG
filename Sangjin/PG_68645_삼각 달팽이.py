def solution(n):
    T = [[0] * i for i in range(1,n+1)]

    #mode1: 좌측 아래로 이동
    #mode2: 맨 밑줄에서 오른쪽으로 이동
    #mode3: 좌측 위로 이동
    mode = 1
    count = 1
    #bottom: mode1->2로 변경시키는 x의 값
    bottom = n-1
    x,y = 0,0
    
    while True:
        #n에 1이 들어온 경우
        if n == 1:
            T = [[1]]
            break
            
        #더 이상 채울 칸이 없으면 종료
        if T[x][y] != 0:
            break
        
        if mode == 1:
            T[x][y] = count
            count += 1
            x,y = x+1,y
            if x == bottom:
                mode = 2
                bottom -= 1
        
        elif mode == 2:
            T[x][y] = count
            count += 1
            x,y = x,y+1
            if y == bottom+1 or T[x][y+1] != 0:
                mode = 3
        else:
            T[x][y] = count
            count += 1
            x,y = x-1,y-1
            if x == 0 or T[x-1][y-1] != 0:
                mode = 1
    #2차원 배열을 1차원 배열로 정렬
    answer = sum(T,[]) #[]에 T의 데이터를 모두 더한다
    return answer