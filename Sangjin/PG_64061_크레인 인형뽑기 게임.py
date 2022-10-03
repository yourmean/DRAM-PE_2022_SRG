#인형을 뽑는 작업
def pick(pick_num, board):
    i = 0 #맨 윗줄부터 검색
    while True:
        if i >= len(board): #탐색 다 해도 없는 경우
            i = -1
            break
        else:
            if board[i][pick_num-1] == 0:
                i += 1
            else:
                break
    return i #건져올릴 인형이 있는 board의 좌표를 return

def solution(board, moves):
    answer = 0
    
    basket = [] #인형을 담을 그릇
    while True:
        if len(moves) == 0:
            break
        else:
            pick_num = moves.pop(0)
            v_loc = pick(pick_num, board)
            
            #건져올릴 인형이 있는 경우
            if v_loc != -1: 
                basket.append(board[v_loc][pick_num-1])
                board[v_loc][pick_num-1] = 0
            
            #바구니에 같은 인형 두 개인 경우
            if len(basket) >= 2:
                if basket[-1] == basket[-2]:
                    basket.pop(-1)
                    basket.pop(-1)
                    answer += 2
            
    
    
    return answer