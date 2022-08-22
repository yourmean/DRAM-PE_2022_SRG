import itertools
n, m = map(int, input().split())
a = list(map(int, input().split()))
black = [x+y+z for x, y, z in itertools.combinations(a, 3)]
result = [k for k in black if k<=m]
print(max(result))
