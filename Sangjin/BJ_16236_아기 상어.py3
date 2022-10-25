from collections import deque

n = int(input())
Map = [list(map(int, input().split())) for i in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
ans = 0

#아기상어의 크기와 위치
baby_size = 2
x, y = 0, 0
for i in range(n):
  for j in range(n):
    if Map[i][j] == 9:
      x, y = i, j

#아기상어가 먹으러 가기 위한 최소 거리 구하기
def eat(x,y,baby_size):
  #거리
  distance = [[0] * n for _ in range(n)]
  #방문 여부
  visited = [[0] * n for _ in range(n)]

  q = deque()
  q.append((x,y))
  visited[x][y] = 1
  fish_list = []

  while q:
    x_now, y_now = q.popleft()
    for i in range(4):
      nx, ny = x_now + dx[i], y_now + dy[i]
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and Map[nx][ny] <= baby_size:
        q.append((nx, ny))
        visited[nx][ny] = 1
        distance[nx][ny] = distance[x_now][y_now] + 1
        if 0 < Map[nx][ny] < baby_size:
          #먹을 수 있는 물고기 위치와 거리 저장
          fish_list.append((nx,ny,distance[nx][ny]))
  #거리가 가장 가까운, 제일 위, 제일 왼쪽인 것이 앞으로 오도록 정렬
  return sorted(fish_list,key=lambda x: (x[2],x[0],x[1]))

while True:
  #popleft를 하기 위해 deque를 사용한다.
  moving = deque(eat(x,y,baby_size))

  #먹을 물고기가 없으면 종료
  if len(moving) == 0:
    break
  #거리가 가장 가까운, 제일 위, 제일 왼쪽인 것을 뽑는다.
  nx, ny, dist = moving.popleft()

  ans += dist
  #물고기 먹은 자리는 0으로 바꿔준다.
  Map[x][y], Map[nx][ny] = 0,0
  x, y = nx, ny
  
  #자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
  cnt += 1
  if cnt == baby_size:
      baby_size += 1
      cnt = 0

print(ans)