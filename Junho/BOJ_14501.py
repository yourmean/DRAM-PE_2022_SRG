#Top - down
n = int(input())
wk = []
for _ in range(n):
    wk.append(list(map(int, input().split())))
dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if i + wk[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], wk[i][1] + dp[i + wk[i][0]])
    
print(dp[0])
