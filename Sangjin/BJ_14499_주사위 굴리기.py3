N, M, x, y, K = map(int, input().split())

Map = []
for i in range(N):
  Map.append(list(map(int, input().split())))

Dice = [0,0,0,0,0,0]
'''
주사위 구조
[0,1,2,3,4,5]
   0    
 1 2 3  윗면이 2, 3은 동쪽, 4는 남쪽을 향한다.
   4
   5
'''

#명령 저장
Com = list(map(int, input().split()))

#주사위의 움직임
def move(a):
  if a == 1: #동쪽
    tem = Dice[1]
    Dice[1] = Dice[5]
    Dice[5] = Dice[3]
    Dice[3] = Dice[2]
    Dice[2] = tem
  elif a == 2: #서쪽
    tem = Dice[1]
    Dice[1] = Dice[2]
    Dice[2] = Dice[3]
    Dice[3] = Dice[5]
    Dice[5] = tem
  elif a == 3: #북쪽
    tem = Dice[0]
    Dice[0] = Dice[2]
    Dice[2] = Dice[4]
    Dice[4] = Dice[5]
    Dice[5] = tem
  elif a == 4: #남쪽
    tem = Dice[0]
    Dice[0] = Dice[5]
    Dice[5] = Dice[4]
    Dice[4] = Dice[2]
    Dice[2] = tem
    
for i in range(K):
  #동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
  if Com[i] == 1:
    if y != M-1: #칸을 벗어나는지 확인용
      move(2) #주사위 돌아감
      y += 1 #주사위 위치 변경
      if Map[x][y] == 0: #이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 
        Map[x][y] = Dice[5]
      else: #0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
        Dice[5] = Map[x][y]
        Map[x][y] = 0
      print(Dice[2]) #주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 출력
  elif Com[i] == 2:
    if y != 0:
      move(1)
      y -= 1
      if Map[x][y] == 0:
        Map[x][y] = Dice[5]
      else:
        Dice[5] = Map[x][y]
        Map[x][y] = 0
      print(Dice[2])
  elif Com[i] == 3:
    if x != 0:
      move(3)
      x -= 1
      if Map[x][y] == 0:
        Map[x][y] = Dice[5]
      else:
        Dice[5] = Map[x][y]
        Map[x][y] = 0
      print(Dice[2])
  elif Com[i] == 4:
    if x != N-1:
      move(4)
      x += 1
      if Map[x][y] == 0:
        Map[x][y] = Dice[5]
      else:
        Dice[5] = Map[x][y]
        Map[x][y] = 0
      print(Dice[2])
  else:
    print("에러")