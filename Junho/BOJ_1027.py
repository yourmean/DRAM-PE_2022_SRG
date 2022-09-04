import itertools
n = int(input())
h = list(map(int, input().split()))
xy = list(enumerate(h))
cnt = [0 for _ in range(n)]
for a, b in itertools.combinations(xy, 2):
    if a[0] > b[0]:
        a, b = b, a
    temp = 0
    for i in range(a[0]+1, b[0]):
        if xy[i][1] >= (b[1] - a[1]) / (b[0] - a[0]) * (xy[i][0] - a[0]) + a[1]:
            temp += 1
    if temp == 0:
        cnt[a[0]] += 1
        cnt[b[0]] += 1

print(max(cnt))
