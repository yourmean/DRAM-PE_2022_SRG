def solution(brown, yellow):
    # yellow = (x-2) * (y-2)
    # brown = 2*(x+y) - 4
    # 결론: yellow + brown = xy
    XY = brown + yellow
    for i in range(1, XY):
        if XY%i == 0:
            j = XY/i
            if j >= i:
                #식이 맞는지 다시 확인
                if brown == 2 * (i + j) - 4:
                    return [j,i]
            
    answer = []
    return answer