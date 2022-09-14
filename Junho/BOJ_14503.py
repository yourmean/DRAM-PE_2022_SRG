x = lambda:map(int, input().split())
N,M  = x()
a,b,c = x()
m = []
d = [-1,0,1,0,-1,0,1,0]
cnt = 0
for _ in range(N):
    m.append(list(x()))
ck = 0
while m[a][b]!=1:
    if m[a][b]==0:
        cnt+=1
    m[a][b]=-1
    ck=1
    for i in range(1,5):
        x = a + d[c-i]
        y = b + d[3-c+i]
        if m[x][y]==0:
            a = x
            b = y
            c = (c-i)%4
            ck= 0
            break
    if ck:
        a+=d[c+2]
        b+=d[c+3]
print(cnt)
