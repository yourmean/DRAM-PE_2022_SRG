n=int(input())

cal=True
m=1 #대각선 맨 위의 1/m에서 m의 값

if(n==1):
  #print("1","/","1") 콤마를 사용하면 공백이 생긴다.
  print("1"+"/"+"1") #덧셈을 사용하면 공백이 생기지 않는다.
else:
  while cal:
    if (m*(m+1)/2 < n and n <= (m+1)*(m+2)/2):
      #1/(m+1)에서 시작
      if (m+1) % 2 == 0: #짝수인 경우
        up = n - m*(m+1)/2 #분모
        dn = (m+2) - up #분자
      else:
        dn = n - m*(m+1)/2 #분모
        up = (m+2) - dn #분자
      print(str(int(up))+"/"+str(int(dn)))
      cal=False
    m+=1  
