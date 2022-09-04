from collections import deque

n = int(input())
graph=[]
for i in range(n):
    graph.append(list( map(int, input()) ))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def octsevntn(graph, a, b):

    global n
    queue = deque()
    queue.append((a,b))
    graph[a][b] = -1
    count = 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
                
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                queue.append((nx, ny))
                count += 1
    
    return count


apt_count = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            apt_count.append(octsevntn(graph, i, j))

s_apt_count = sorted(apt_count)
r = len(s_apt_count)
print(r)
for i in range(r):
    print(s_apt_count[i])
