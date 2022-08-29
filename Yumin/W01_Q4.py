# 상진이와 창원이의 카드 게임

n, m = map(int, input().split(" "))

result = 0

for i in range(n):
    arr = list(map(int, input().split(" ")))
    min_value = min(arr)
    result = max(result, min_value)

print(result)