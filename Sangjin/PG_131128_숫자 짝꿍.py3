def solution(X, Y):
    XX = list(X)
    YY = list(Y)
    
    #내림차순으로 정렬
    XX.sort(reverse=True)
    YY.sort(reverse=True)
    
    X_i, Y_i = 0, 0
    #짝꿍을 넣을 자리
    XY = []
    while True:
        if XX[X_i] > YY[Y_i]:
            X_i += 1
        elif XX[X_i] < YY[Y_i]:
            Y_i += 1
        elif XX[X_i] == YY[Y_i]:
            XY.append(XX[X_i])
            X_i += 1
            Y_i += 1
        else:
            print("ERR")
        
        if X_i >= len(XX) or Y_i >= len(YY):
            break
    
    #예외적인 경우에 대한 처리
    if XY == []:
        XY = ['-1']
    elif XY[0] == '0':
        XY = ['0']
    
    
    answer = ''.join(XY)
    return answer