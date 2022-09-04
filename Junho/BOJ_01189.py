from collections import deque
import copy

apb = ['a','b','c','d','e','f','g','h','i',
       'j','k','l','m','n','o','p','q','r',
       's','t','u','v','w','x','y','z']

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

r,c,k = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(str, input())))

queue = deque()

if graph != [['T']]:
    graph[r-1][0] = apb[0]
answer = []
step = 0


before_graph = copy.deepcopy(graph)

def bfs(b_graph, b_step, b_queue):
    
    global answer    
    tmp_graph = copy.deepcopy(b_graph)
    bfs_step = b_step
    queue = b_queue
  
    while queue:
        x, y = queue.popleft()
        bfs_step += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if tmp_graph[nx][ny] == '.':
                tmp_graph[nx][ny] = apb[bfs_step]
                
                if nx == 0 and ny == c-1:
                    answer.append(bfs_step)
                    
                queue.append((nx, ny))
                bfs(tmp_graph, bfs_step, queue)
                tmp_graph[nx][ny] = '.'

queue.append((r-1, 0))
bfs(before_graph, step, queue)
count = 0
for i in answer:
    i += 1
    if i == k:
        count += 1

if r == 1 and c == 1 and k == 1 and graph != [['T']]:
    count = 1
elif r == 1 and c == 1 and graph == [['T']]:
    count = 0
    
print(count)
