n = int(input())
p = [1,1,1,2,2,3,4,5,7,9]

pn = []
for i in range(n):
    pn.append(int(input()))

mp = max(pn)
if mp >= 10:
    for i in range(10, mp):
        p.append(p[i-1]+p[i-5])
    
    for i in pn:
        print(p[i-1])
else:
    for i in pn:
        print(p[i-1])
