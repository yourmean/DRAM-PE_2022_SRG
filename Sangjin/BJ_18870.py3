import copy

n=int(input())
#입력된 목록
L1 = list(map(int,input().split()))
#목록을 오름차순으로 정렬
L2 = copy.deepcopy(L1)
L2.sort()
#압축된 숫자 저장
L3 = [0 for i in range(n)]
start = 0
for i in range(n):
  if i == 0:
    L3[i] = 0
  else:
    if L2[i]==L2[i-1]:
      L3[i]=L3[i-1]
    else:
      L3[i]=L3[i-1]+1

#L2와 L3로 리스트 만들기
# print(L2)
# print(L3)
L_dic = dict(zip(L2,L3))
# print(L_dic)

      
#답안
L4 = [0 for i in range(n)]
for i in range(n):
  L4[i]=L_dic[L1[i]]
  
print(*L4)