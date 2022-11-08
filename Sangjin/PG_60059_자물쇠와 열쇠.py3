def CheckLock(N, lock3): #열쇠를 넣었을 때 중앙의 lock 부분이 모두 1이 되는지 확인
    check = True
    for i in range(N, 2*N):
        for j in range(N, 2*N):
            if not lock3[i][j]:
                check = False
    return check
    
def Spin_Clockwise(key): #열쇠를 시계방향으로 90도 회전시킨다
    key = list(map(list, zip(*key[::-1])))
    return key

def solution(key, lock):
    answer = False
    #key와 lock의 크기
    M, N = len(key), len(lock)
    
    #lock 길이를 가로세로 3배씩 늘린 구역을 만든다.
    lock3 = [[0 for i in range(3*N)] for j in range(3*N)]
    #가운데에 lock을 넣는다.
    for i in range(N):
        for j in range(N):
            lock3[N+i][N+j] = lock[i][j]

    #key를 lock3 위로 지나가게 하면서 key가 1인 부분을 처리함
    #key:1, lock3:1 -> 0으로 변환
    #key:1, lock3:0 -> 1로 변환
    for s in range(4):
        for i in range(3*N-M+1):
            for j in range(3*N-M+1):
                for k_i in range(M):
                    for k_j in range(M):
                        if key[k_i][k_j] == 1:
                            if lock3[i+k_i][j+k_j] == 1:
                                lock3[i+k_i][j+k_j] = 0
                            else:
                                lock3[i+k_i][j+k_j] = 1
                #lock3 변환 완료 후 자물쇠를 열 수 있는지 체크
                if CheckLock(N, lock3):
                    answer = True   
                
                #열쇠를 꽂은 부분을 원상복귀시킨다.
                for k_i in range(M):
                    for k_j in range(M):
                        if key[k_i][k_j] == 1:
                            if lock3[i+k_i][j+k_j] == 1:
                                lock3[i+k_i][j+k_j] = 0
                            else:
                                lock3[i+k_i][j+k_j] = 1
        key = Spin_Clockwise(key) #key를 시계방향으로 90도 회전시켜서 다시 시도해본다.
    
    return answer