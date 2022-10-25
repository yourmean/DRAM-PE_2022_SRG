from collections import deque

n = int(input())
Map = [list(input()) for i in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

#R을 G로 모두 변경한 맵 생성
RG_Map = [item[:] for item in Map]
for i in range(n):
  for j in range(n):
    if RG_Map[i][j] == "R":
      RG_Map[i][j] = "G"

visited = [[False] * n for _ in range(n)]

#구역 확정 알고리즘
def bfs(x, y, color, M):
  #같은 색깔로 모인 구역을 d에 담는다.
  d = deque()
  d.append([x, y])
  while d:
    search = d.popleft()
    x = search[0]
    y = search[1]
    #visited에 해당 좌표를 True로 저장
    if visited[x][y] == False:
      visited[x][y] = True
      for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
          if M[nx][ny] == color:
            d.append([nx, ny])

# 1번: 색약이 아닌 경우
count = 0
for i in range(n):
  for j in range(n):
    if visited[i][j] == False:
        color = Map[i][j]
        bfs(i, j, color, Map)
        count += 1
      
# 2번: 색약인 경우
visited = [[False] * n for _ in range(n)]  
count2 = 0
for i in range(n):
	for j in range(n):
            if visited[i][j] == False:
              color = RG_Map[i][j]
              bfs(i, j, color, RG_Map)
              count2 += 1


print(count,count2)