arr = [[0 for _ in range(101)] for _ in range(101)]
N = int(input())
for _ in range(N):
    x, y = list(map(int, input().split()))
    
    for s in range(x, x+10):
        for t in range(y, y+10):
            arr[s][t] = 1

answer = 0

for k in arr:
    answer += k.count(1)

print(answer)
