n = int(input())
board = [list(map(int,input().split())) for _ in range(6)]

max_width, max_width_idx = 0, 0
max_height, max_height_idx = 0, 0

for i in range(len(board)):
    if board[i][0] in [1,2]:
        if board[i][1] > max_width:
            max_width = board[i][1]
            max_width_idx = i
    else:
        if board[i][1] > max_height:
            max_height = board[i][1]
            max_height_idx = i

min_width = abs(board[(max_width_idx-1) % 6][1] - board[(max_width_idx+1) % 6][1])
min_height = abs(board[(max_height_idx-1) % 6][1] - board[(max_height_idx+1) % 6][1])


print((max_height*max_width) - (min_height * min_width)*n)



# (-1)%6 = 5
