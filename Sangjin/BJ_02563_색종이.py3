N = int(input())
L = [list(map(int, input().split())) for i in range(N)]

MAP = [[ 0 for _ in range(101)] for _ in range(101)]
for i in range(len(L)):
  for x in range(10):
    for y in range(10):
      MAP[L[i][0] + x][L[i][1] + y] = 1

Total = 0
for i in range(101):
  Total+=sum(MAP[i])
print(Total)