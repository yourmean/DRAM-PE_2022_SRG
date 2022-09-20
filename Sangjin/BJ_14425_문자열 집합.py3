N,M = map(int,input().split())

#set 사용
N_list = set([input() for _ in range(N)]) #N줄을 입력한다

M_list = [input() for _ in range(M)] #M줄을 입력한다

ans = 0
for i in range(M):
    if M_list[i] in N_list: #for문 이중으로 돌리면서 다 비교해준다.
      ans += 1

print(ans)