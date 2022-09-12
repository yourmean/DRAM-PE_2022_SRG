# 세로 크기 N, 가로 크기 M
N, M = map(int, input().split())
# 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d
# d가 (0, 1, 2, 3) = (북, 동, 남, 서)
r, c, d = map(int, input().split())

#House 맵
H = [list(map(int, input().split())) for _ in range(N)]

#청소중이냐
Cleaning = True
#청소한 타일 개수
tile = 1 #시작점은 무조건 청소
H[r][c] = 2
#방향전환은 왼쪽으로
def turn(x):
  if x==0:
    return 3
  elif x==1:
    return 0
  elif x==2:
    return 1
  elif x==3:
    return 2
#4방향이 모두 막혀있는지 확인
turn_count = 0 #4가 되면 

  # 작동 잘 되는지 확인용
  # print(H)
  # print(r,c,d)
  # print(H[r][c-1])
  # print(H[r][c+1])
  # print(H[r-1][c])
  # print(H[r+1][c])
  # print('turn count:' , turn_count)
  # print('tile: ', tile)
  # print(Cleaning)

while Cleaning:
  #왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 청소를 진행한다. 
  #여기가 2번 시작
  if (d==0 and H[r][c-1]==0) or (d==1 and H[r-1][c]==0) or (d==2 and H[r][c+1]==0) or (d==3 and H[r+1][c]==0):
    turn_count = 0 #4번 연달아 회전했는지 확인하는 숫자 초기화
    
    d = turn(d)
    if d==0:
      r -= 1
    elif d==1:
      c += 1
    elif d==2:
      r += 1
    elif d==3:
      c -= 1
    else:
      print('Error')
      break
    H[r][c] = 2 #청소한 곳은 2로 표시
    tile += 1

  # 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
  # elif (d==0 and H[r][c-1]!=0) or (d==1 and H[r+1][c]!=0) or (d==2 and H[r][c+1]!=0) or (d==3 and H[r-1][c]!=0):
  else:
    d = turn(d)
    # 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    turn_count += 1
    if turn_count == 4:
      #네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
      if d==0:
        if H[r+1][c]==1:
          Cleaning = False
          break
        else:
          r += 1
          turn_count = 0 #4번 연달아 회전했는지 확인하는 숫자 초기화
      elif d==1:
        if H[r][c-1]==1:
          Cleaning = False
          break
        else:
          c -= 1
          turn_count = 0 #4번 연달아 회전했는지 확인하는 숫자 초기화
      elif d==2:
        if H[r-1][c]==1:
          Cleaning = False
          break
        else:
          r -= 1
          turn_count = 0 #4번 연달아 회전했는지 확인하는 숫자 초기화
      elif d==3:
        if H[r][c+1]==1:
          Cleaning = False
          break
        else:
          c += 1
          turn_count = 0 #4번 연달아 회전했는지 확인하는 숫자 초기화
      else:
        print("에러")
        break
    if turn_count > 4:
      print('turn_count ERROR')
      break
      
print(tile)