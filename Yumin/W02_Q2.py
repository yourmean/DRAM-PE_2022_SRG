# 영호는 삼각형을 좋아해

MOD = 1000000007

def dsum(L):
    if not L: return 0
    SL = sum(L)
    A = SL**3
    B = sum(i**2 for i in L) * SL
    C = sum(i**3 for i in L)
    return ((A-3*B+2*C)//6) % MOD

from sys import stdin
input = stdin.readline
from fractions import gcd

slope = {}
for i in range(int(input())):
    a, b, c = map(int,input().split())
    if b == 0:
        res = float('inf')
    else:
        g = gcd(a, b)
        res = (a//g, b//g)
    slope[res] = slope.get(res, 0) + 1
print(dsum(slope.values()))