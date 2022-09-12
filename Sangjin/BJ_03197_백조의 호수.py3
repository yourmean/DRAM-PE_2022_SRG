from collections import deque

R, C = map(int, input().split())

si, sj = 0, 0  #백조 한 마리의 위치(둘 중 하나)
date = 0 #날짜
dx, dy = (0, -1, 0, 1), (-1, 0, 1, 0)   #상하좌우 방향을 의미
map1 = [list(input().strip()) for _ in range(R)] #맵을 받아서 입력

w_c = [[False] * C for _ in range(R)] #물이 있는 곳은 True
s_c = [[False] * C for _ in range(R)] #백조가 갈 수 있는 곳은 True

w_o, w_x = deque(), deque() #물이 있는 공간 구분용(있음/없음)
s_1, s_2 = deque(), deque() #백조가 갈 수 있는 공간 구분용

dx, dy = (1,-1,0,0), (0,0,-1,1) #4방향 이동

def water():
    while w_o:
        x, y = w_o.popleft()   #왼쪽에서 pop
        map1[x][y] = '.' #입력된 좌표에 물을 입력
        for i in range(4):   #4방향 진행
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or w_c[nx][ny]:
                continue   #nx, ny가 범위를 넘어가거나 이미 거쳐간 좌표는 넘어간다.
            if map1[nx][ny] == '.':   #물이 있다면 w_o에 추가
                w_o.append((nx, ny))
            else:   #물이 없다면 w_x에 추가
                w_x.append((nx, ny))
            w_c[nx][ny] = True #거쳐간 곳 표시
          
def swan():
  while s_1:
    x, y = s_1.popleft()
    if x == si and y == sj:   #백조끼리 만나면 true를 리턴
      return True
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if nx < 0 or nx >= R or ny < 0 or ny >= C or s_c[nx][ny]: #이미 거쳐간 좌표는 넘어간다.
        continue
      if map1[nx][ny] == '.': #물이면 건너갈 수 있다.
        s_1.append((nx, ny))
      else:
        s_2.append((nx, ny))
      s_c[nx][ny] = True #거쳐간 곳 표시
  return False #백조끼리 못 만나면 False 리턴

for i in range(R):
  for j in range(C):
    if map1[i][j] == 'L':   #백조의 위치를 찾은 경우
      if not s_1:   #s1의 큐가 비었다면, 백조 위치 저장
        s_1.append((i, j))
        s_c[i][j] = True #백조 위치
      else:   #나머지 백조의 위치를 si와 sj에 저장(도착지가 된다)
        si, sj = i, j
      map1[i][j] = '.'   #백조의 위치엔 물이 있다
    if map1[i][j] == '.':   #물이 있는 경우
      w_o.append((i, j))
      w_c[i][j] = True   #물의 위치를 true로 변경

while True:
    water()
    if swan():   #백조가 만나면 true를 return하므로 while문을 break
        break
    date += 1   #날짜 추가
  
    #다음날 준비
    w_o = w_x #빙판을 w_o에 넣어준다  
    s_1 = s_2 #백조가 못간 길을 s_1에 넣어준다
    w_x = deque()   #초기화
    s_2 = deque()   #초기화

#print(map1)
#print(w_c)
#print(s_c)
print(date)