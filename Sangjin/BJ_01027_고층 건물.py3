N = int(input())
#Buildings
B = list(map(int,input().split()))
#각 빌딩에서 보이는 다른 빌딩의 수
BB = [0 for _ in range(N)]

for i in range(N):
  start = True
  s_n = 1 #1씩 왼쪽으로 가면서 기울기 측정
  min_slope = B[i] #최소 기울기 기록
  #왼쪽에 있는 건물들
  while start:
    if i - s_n >= 0:
      slope = (B[i] - B[i - s_n]) / (s_n)
      if s_n == 1:
        BB[i] += 1
        min_slope = slope
      else: #앞서 나온 최소 기울기보다 더 낮은 수여야 한다.
        if slope < min_slope:
          BB[i] += 1
          min_slope = slope
      s_n += 1
      #이런 식으로 0번 건물까지 탐색
    else:
      start = False #탐색 중지

  start = True
  s_n = 1
  max_slope = -B[i] #최대 기울기 기록
  #오른쪽에 있는 건물들
  while start:
    if i + s_n <= N-1:
      slope = (B[i + s_n] - B[i]) / (s_n)
      if s_n == 1:
        BB[i] += 1
        max_slope = slope
      else: #앞서 나온 최대 기울기보다 더 큰 수여야 한다.
        if slope > max_slope:
          BB[i] += 1
          max_slope = slope
      s_n += 1
      #이런 식으로 N-1번 건물까지 탐색
    else:
      start = False #탐색 중지

print(max(BB)) 