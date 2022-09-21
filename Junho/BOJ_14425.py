n, m = map(int, input().split())
s = dict()
count = 0

for _ in range(n):
    word = str(input())
    s[word] = True

for _ in range(m):
    wordss = str(input())
    if wordss in s.keys():
        count += 1


print(count)
