# ------------------------2477번. 참외밭------------------------#
# 1m^2.의 넓이에 자라는 참외 개수 헤아린 다음 참외밭 넓이 구하면 비례식 이요해 참외 총 개수 구함
# ㄱ이나 ㄱ을 90도, 180도, 270도 회전한 모양의 육각형
# 참외밭 면적이 6800m^2이고 1m^2의 넓이에 자라는 참외 개수가 7개라면 참외 개수는 47600개
# 임의의 한 꼭지점에서 출발하여 반시계방향으로 둘레를 돌며 지나는 변의 방향과 길이 
# 6개가 순서대로 주어짐. 
# 참외개수: 1<=K<=20 / 변의 방향과 길이=1이상 500이하의 정수
# 변의방향에서 동쪽은1, 서쪽2, 남쪽3, 북쪽 4

# sys안먹어서 여기서 풀 땐 이걸로 돌려
K= int(input())
w=[]
h=[]
total=[]
for i in range(6):
    dir,lg=map(int,input().split())
    if dir==1 or dir==2:
        h.append(lg)
        total.append(lg)
    else:
        w.append(lg)
        total.append(lg)

xw=total.index(max(w))+3  ; xh=total.index(max(h))+3

if xw>5 :
    xw=xw-6
if xh>5:
    xh=xh-6
else: 
    xw=xw
    xh=xh
    
box=max(w)*max(h)-total[xw]*total[xh]
print(K*box)

# 가장 큰 변 index+3이 빼야할 사각형의 가로 세로

###  백준 제출용 ###
import sys
K= int(sys.stdin.readline())
w=[]
h=[]
total=[]
for i in range(6):
    dir,lg=map(int, sys.stdin.readline().split())
    if dir==1 or dir==2:
        h.append(lg)
        total.append(lg)
    else:
        w.append(lg)
        total.append(lg)

xw=total.index(max(w))+3  ; xh=total.index(max(h))+3
if xw>5 :
    xw=xw-6
if xh>5:
    xh=xh-6
else: 
    xw=xw
    xh=xh

box=max(w)*max(h)-total[xw]*total[xh]
print(K*box)