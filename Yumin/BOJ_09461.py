ans = [0 for i in range(101)]
ans[1], ans[2], ans[3]  = 1, 1, 1

for i in range(0, 98):
    ans[i+3] = ans[i] + ans[i+1]

for i in range(int(input())):
    n = int(input())
    print(ans[n])
