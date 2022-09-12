N, K = map(int, input().split())
list = [list(map(int, input().split())) for _ in range(N)]

#dp[i][j]: i번째 물건까지 검토, 무게 j까지 들 수 있는 경우 최대가치
dp = [[0 for j in range(K)] for i in range(N)]

for i in range(N):
  for j in range(K):
    #물건의 무게
    w = list[i][0] 
    #물건의 가치
    v = list[i][1]

    if i == 0: #첫 번째 항목
      if w-1 > j: #들 수 있는 무게 초과
        # dp는 인덱스가 0부터 시작하므로 w 대신 w-1을 사용
        dp[i][j] = 0
      else:
        dp[i][j] = v #가치를 넣어준다
    
    else:
      if w-1 > j: #들 수 있는 무게 초과
        dp[i][j] = dp[i-1][j]
      elif w-1 == j:
        dp[i][j] = max(dp[i-1][j], v)
      else:
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[N-1][K-1])