N = int(input())
#스케줄
sc = [list(map(int, input().split())) for _ in range(N)]

income = 0
Max_price = 0
#n일차에 상담을 하는 경우 (n: 0 ~ N-1)
def cal(n):
  global income
  next_day = n + sc[n][0]
  if next_day > N:
    if n + 1 >= N:
      #계산끝
      cal_Max(income)
    else:
      cal(n+1)

  elif next_day == N: #N과 일치하는 경우도 고려
    income += sc[n][1]
    #계산끝
    cal_Max(income)
    #돌아올땐 더해준 만큼 빼준다
    income -= sc[n][1]
    if n + 1 >= N:
      return #뒤로 돌아간다
    else:
      cal(n + 1)
    
  else:
    income += sc[n][1]
    cal(next_day)
    #돌아올땐 더해준 만큼 빼준다
    income -= sc[n][1]
    if n + 1 >= N:
      #계산끝
      cal_Max(income)
    else:
      cal(n+1)

def cal_Max(new_price):
  global Max_price
  if Max_price < new_price:
    Max_price = new_price

cal(0)
print(Max_price)