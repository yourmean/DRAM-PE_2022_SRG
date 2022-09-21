num = list(range(1,31))

for _ in range(28):
    a = int(input())
    num.remove(a)

for i in range(len(num)):
    print(num[i])
