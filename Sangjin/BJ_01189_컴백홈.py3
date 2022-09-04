r,c,k = map(int, input().split())
#한 글자씩 나눠서 저장
t_map = [list(input()) for _ in range(r)] 

ans = 0

def r_f(x, y, step):
    global ans
    if step == k: #목표 이동횟수
        if (x, y) == (0, c - 1):
          ans += 1 #조건에 맞으므로 횟수를 늘려준다.
    else:
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and t_map[nx][ny] != 'T':
                t_map[nx][ny] = 'T'
                r_f(nx, ny, step + 1)
                t_map[nx][ny] = '.'

t_map[r - 1][0] = 'T' # 시작 지점 방문 처리
r_f(r - 1, 0, 1) #시작지점도 이동횟수 1회를 먹고 들어간다.
print(ans)