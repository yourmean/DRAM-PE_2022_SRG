#www.acmicpc.net/source/24821079
N = int(input())
def digit_666(num):
    s = 10;
    d = 0
    while int(num/s) >= 666:
        if int(num/s) % 1000 == 666:
            d = s
        s *= 10
    return d

title = 666
n = 1
while n < N:
    title += 1000
    d = digit_666(title)
    if d == 0:
        n += 1
    else:
        if (n + d >= N):
            title = int(title/d) * d
            title += (N - n - 1)
            n = N
        else:
            n += d
print(title)
