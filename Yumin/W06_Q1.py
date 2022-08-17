# 시인 김준호

N = int(input())

cost = []
for n in range(N) :
    t = map(int, input().split())
    cost.append(list(t))

memo = [cost[0]]

for n in range(1,N):
    tmp = []
    for i in range(3):
        a = 1000000
        for j in range(3):
            if i==j:
                continue
            a = min(a, memo[n-1][j]+cost[n][i])
        tmp.append(a)
    memo.append(tmp)

print(min(memo[n]))