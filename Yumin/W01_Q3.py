# 서희의 계산기

num = int(input())
answer = 0
for n in range(1, num+1):
    if n <= 99:
        answer += 1

    else:
        nums = list(map(int, str(n)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            answer += 1

print(answer)