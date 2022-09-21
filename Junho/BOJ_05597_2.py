import sys

a, b = set(range(1, 31)) - set(map(int, sys.stdin))
print(min(a, b))
print(max(a, b))
