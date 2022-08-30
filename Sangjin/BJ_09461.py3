#규칙
#f(n)+f(n-4)=f(n+1)

#시간이 오래 걸리므로 메모이제이션을 수행해야 한다.
mem = {1:1, 2:1, 3:1, 4:2, 5:2}

def sol(m):
  if m in mem: #이미 딕셔너리에 있는 숫자는 여기서 사용한다.
    return(mem[m])
  else:
    mem[m] = sol(m-1)+sol(m-5)
    return(mem[m])

n=int(input())
for i in range(n):
  m = int(input())
  print(sol(m))