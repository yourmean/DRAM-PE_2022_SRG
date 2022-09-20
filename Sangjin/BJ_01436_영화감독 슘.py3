N = int(input())
n_666 = [0 for _ in range(10001)] #10000 range로 하면 indexError가 뜬다.

#666이 들어가는지 확인
def find_six(x):
  n_list = []
  triple = 0
  for j in str(x):
    if j == '6': #str에서 하나씩 가져오므로 6이 아니라 '6'을 찾는다.
      triple += 1
    else:
      triple = 0
      
    if triple == 3: #연달아 6이 3번 나온 경우 True를 리턴하고 종료
      return(True)
  return(False)
  

count = 1
num = 666 #가장 작은 수 666부터 시작
while count <= N:
  if find_six(num): #해당 숫자에 666이 있는지 확인
    n_666[count] = num #n번째 숫자는 n+1번째 리스트에 저장
    count+=1
  num+=1

print(n_666[N])