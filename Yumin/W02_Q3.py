# 바쁜 총무 솔이

n, k = map(int, input().split())

def dp(n,k):
    memo = [1 for i in range(n+2)]
    for a in range(1, k):
        tmp = []
        for b in range(n+1):
            tmp.append(sum(memo[0:b+1]))
        memo = tmp
    #print(a, memo)
    return memo[-1]
print(dp(n,k)%10000)
