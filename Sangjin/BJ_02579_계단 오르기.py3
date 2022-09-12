N = int(input())
step = [int(input()) for _ in range(N)] #계단 숫자 입력받기
M_step = [int(0) for _ in range(N)] #step별 최대 점수를 기록하는 공간

M_step[0] = step[0] #1번째 계단
if N > 1:
  M_step[1] = step[0] + step[1]
  if N > 2:
    M_step[2] = max(M_step[0] + step[2], step[1] + step[2])

if N > 3:
  #각 단계별로 최대 점수를 기록한다.
  for n in range(3,N):
    M_step[n] = max(M_step[n-3] + step[n-1] + step[n], M_step[n-2] + step[n]) 

print(M_step[N-1])