def solution(board,moves) :
    stack=[]
    result=0
    for i in moves :
        for j in range(0,len(board)) :
            if board[j][i-1]==0 :
                pass
            else:
                stack.append(board[j][i-1])
                board[j][i-1]=0  #뺐으니까 0 만들기
                break   #2번째 for문에서 빠져나오기
        if len(stack)>=2 and stack[-1]==stack[-2] :
            stack.pop()
            stack.pop()
            result+=2
    return result