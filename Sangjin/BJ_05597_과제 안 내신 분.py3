students = set([int(input()) for _ in range(28)]) #제출한 28명의 번호 입력

for i in range(1,31): #1부터 30까지
  if i not in students:
    print(i)
  else:
    # print('not', i)
    () #버그 찾는 용으로 사용