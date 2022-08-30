n = int(input())
ab = []
for i in range(6):
  a, b = map(int, input().split())
  ab.append([a,b])

#    북           4
# 서   동     2     1
#    남           3

# 서남동을 찾는다                    
# (동 남)동북 서남동 ┐ 31'42'31 (가장 긴 사각형 표시)
# 동 (북동)북 서남동 ┌ 414'23'1
# 동 북서(남 서)남동 ┘ 4'2323'1
# 동 북(서북) 서남동└  4242'31'
for i in range(6): #231을 찾기 위해 배열을 한 번 반복하여 늘려준다.
  ab.append(ab[i])

find = True
i = 0
while find:
  if ab[i][0] == 2 and ab[i+1][0] == 3 and ab[i+2][0] == 1:
    find = False
  else:
    i += 1
#ab[i] 의 i, i+1, i+2가 서남동으로 이동한 부분
space = 0 #면적
if ab[i+3][0]==3: #남동북서남동
  space = ab[i+5][1]*ab[i][1] - ab[i+2][1]*ab[i+3][1]
elif ab[i+4][0]==1: #북동북서남동
  space = ab[i][1]*ab[i+1][1] - ab[i+3][1]*ab[i+4][1]
elif ab[i+5][0]==3: #북서남서남동
  space = ab[i+2][1]*ab[i+3][1] - ab[i][1]*ab[i+5][1]
else: #북서북서남동
  space = ab[i+1][1]*ab[i+2][1] - ab[i+4][1]*ab[i+5][1]

print(space*n) #참외의 개수
  