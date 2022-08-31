n = int(input())
line = list(map(int, input().split())).sort()

ans = 0
for i in range(1, n+1):
    ans += sum(line[:i])
print(ans)
