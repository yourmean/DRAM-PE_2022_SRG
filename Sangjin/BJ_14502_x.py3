from itertools import combinations
import copy

n,m = input().split()
n=int(n)
m=int(m)
#n x m의 공간이 만들어진다

Map1=[]
for i in range(n):
    Map1.append(list(map(int, input().split())))

# print(Map1)

#Map1에서 빈 칸의 좌표를 모두 구한다
Bin=[]
Bin_num=0 #조합의 개수
for a in range(n):
    for b in range(m):
      if Map1[a][b]==0:
        Bin.append([a,b])
Bin_3 = list(combinations(Bin, 3)) #빈 칸을 3개씩 고른 조합
Bin_num = len(Bin_3) #조합의 개수를 넣어준다

      
#바이러스가 최대로 퍼진 상황을 리턴
def active_virus(X,n,m):
  for i in range(64):
    for a in range(n):
      for b in range(m):
        if X[a][b]==2:
          if a!=0:
            if X[a-1][b]==0:
              X[a-1][b] = 2
          if a!=n-1:
            if X[a+1][b]==0:
              X[a+1][b] = 2
          if b!=0:
            if X[a][b-1]==0:
              X[a][b-1] = 2
          if b!=m-1:
            if X[a][b+1]==0:
              X[a][b+1] = 2
  return X

# 실행: active_virus(Map1,n,m)
  
  
#0의 개수 세기
def Zero_Num(X,n,m):
  Zero=0
  for a in range(n):
    for b in range(m):
      if X[a][b]==0:
        Zero+=1
  return Zero

Max_Zero_Num = 0
for i in range(Bin_num):
  Map2 = copy.deepcopy(Map1) #Map1을 복사(Deep 복사를 해야 한다)
  #3개 점을 1로 만든다(벽을 만든다)
  Map2[Bin_3[i][0][0]][Bin_3[i][0][1]]=1
  Map2[Bin_3[i][1][0]][Bin_3[i][1][1]]=1
  Map2[Bin_3[i][2][0]][Bin_3[i][2][1]]=1
  # print(Map2)
  # print(Map1)
  active_virus(Map2,n,m) #바이러스를 퍼뜨린다
  New_Zero_Num = Zero_Num(Map2,n,m) #0의 개수를 센다
  # print(New_Zero_Num)
  if Max_Zero_Num < New_Zero_Num:
    Max_Zero_Num = New_Zero_Num
  
  
print(Max_Zero_Num) #안전 영역의 최대 크기