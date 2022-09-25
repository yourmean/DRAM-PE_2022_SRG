def solution(board, moves):
    basket = []
    answer = 0

    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                basket.append(board[i][m-1])
                board[i][m-1] = 0

                if len(basket)>=2 and  basket[-2] == basket[-1]:
                    answer += 2
                    del basket[-2:]
                break
    return