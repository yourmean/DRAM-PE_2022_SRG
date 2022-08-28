n = int(input())
m = list(map(int, input().split()))
m = sorted(m)
a = []
a.append(m[0])
for k in range(1,n):
    a.append(a[k-1]+m[k])
print(sum(a))
