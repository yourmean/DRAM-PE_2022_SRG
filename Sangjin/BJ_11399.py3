n=int(input())
L=list(map(int, input().split()))

L.sort() #숫자를 오름차순으로 정렬

ans=0
#맨 앞에 있는 숫자는 리스트의 길이만큼 반복해서 더해줌
#맨 끝에 있는 숫자는 한 번만 더해줌
for i in range(len(L)):
  ans+=(len(L)-i)*L[i]

print(ans)
 
