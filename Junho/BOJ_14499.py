n, m, x, y, z = map(int, input().split())

graph = []
dx = [0, 0, -1, 1] #북, 남
dy = [1, -1, 0, 0] #동, 서
dice = [0, 0, 0, 0, 0, 0]
        
for i in range(n):
    graph.append(list(map(int, input().split())))

    
ord_list = list(map(int, input().split()))

def dice_turn(d):
    v1, v2, v3, v4, v5, v6 = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    
    if d == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = v4, v2, v1, v6, v5, v3

    elif d == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = v3, v2, v6, v1, v5, v4

    elif d == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = v5, v1, v3, v4, v6, v2

    else: #남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = v2, v6, v3, v4, v1, v5


for i in ord_list:
    x += dx[i-1]
    y += dy[i-1]
    
    if x < 0 or x >= n or y < 0 or y >= m:
        x -= dx[i-1]
        y -= dy[i-1]
        continue

    dice_turn(i)

    if graph[x][y] == 0:
        graph[x][y] = dice[5]
    else:
        dice[5] = graph[x][y]
        graph[x][y] = 0

    print(dice[0])
