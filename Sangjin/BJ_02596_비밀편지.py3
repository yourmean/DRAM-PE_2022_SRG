n = int(input())
M = input()

#순서대로 A~H
M_A = ['000000','001111','010011','011100','100110','101001','110101','111010']

#표현형: ['0', '0', '1', ... ]
M_Q = list(M)

ans = []

for i in range(n):
  word = i+1
  for k in range(8): #A~H까지 총 8개 글자와 비교
    M_AK = list(M_A[k])
    cnt = 0 #다른 개수
    for j in range(6):
      num  = i*6 + j
      if M_AK[j] != M_Q[num]:
        cnt += 1
    if cnt <= 1:
      if k == 0:
        word = "A"
      elif k == 1:
        word = "B"
      elif k == 2:
        word = "C"
      elif k == 3:
        word = "D"
      elif k == 4:
        word = "E"
      elif k == 5:
        word = "F"
      elif k == 6:
        word = "G"
      else:
        word = "H"
  if word == i+1:
    ans = str(word)
    break
  else:
    ans.append(word)
print(''.join(ans)) #list의 내용물을 한 단어로 출력
      
