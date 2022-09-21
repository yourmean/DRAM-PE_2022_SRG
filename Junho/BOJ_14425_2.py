import sys

N, M = map(int, sys.stdin.readline().strip().split())
str = sys.stdin.read().split()
S, command = set(str[:N]), str[N:]
print(sum(1 for i in command if i in S))
