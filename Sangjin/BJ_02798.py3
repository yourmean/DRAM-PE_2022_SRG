n,m = input().split()
n=int(n)
m=int(m)
#n개 숫자가 주어진다
#m을 넘지 않는 수 만들기
L = list(map(int,input().split()))

mx=0
for i in range(n):
  for j in range(n):
    if j==i:
      continue
    for k in range(n):
      if k==i or k==j:
        continue
      if L[i]+L[j]+L[k]>mx and L[i]+L[j]+L[k]<=m:
        mx = L[i]+L[j]+L[k]

print(mx)
