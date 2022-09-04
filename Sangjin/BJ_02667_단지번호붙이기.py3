N = int(input())

Map = [list(map(int, input())) for _ in range(N)]
Map2 = [[0 for j in range(N)] for i in range(N)]
#각 단지별 집의 개수 저장
C = []
count = 0

def grouping(i, j, group):
  global count
  Map2[i][j] = group
  count += 1 #집의 개수 1 증가
  di = [-1,1,0,0]
  dj = [0,0,-1,1]
  for k in range(4):
    ni = i + di[k]
    nj = j + dj[k]
    if ni < 0 or ni >= N or nj < 0 or nj >= N:
      continue
    if Map[ni][nj] == 1 and Map2[ni][nj] == 0:
      grouping(ni, nj, group) #재귀적으로 구성


group = 0 #단지의 개수
for i in range(N):
  for j in range(N):
    if Map[i][j] == 1 and Map2[i][j] == 0:
      group += 1
      grouping(i, j, group) #1로 붙은 영역을 단지로 지정
      C.append(count)
      count = 0 #집의 개수 리셋


# print(Map)
# print(Map2)
print(group) #총 단지 수 출력

C.sort(reverse=False) #집의 개수를 오름차순으로 정렬
for _ in range(len(C)):
  print(C[_])
  

