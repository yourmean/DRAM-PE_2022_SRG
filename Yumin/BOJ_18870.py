# 참고 : https://gudwns1243.tistory.com/52

n = int(input())
num_list = list(map(int, input().split()))

num_order = sorted(list(set(num_list)))
ans = {num_order[i] : i for i in range(len(num_order))}
for i in num_list:
    print(ans[i], end = ' ')
