def solution(s):
    answer = 1E9
    if len(s) == 1:
        return 1
    else:
      # //: 나눗셈의 몫 구하기
      #n의 범위: 1~s길이의 절반까지
        result = 1000000
        for i in range(1,len(s)//2+1):
            #줄어든 string
            shorten = ''
            #중복되는 단어 개수
            cnt = 1
            #중복되는 string
            temp = s[:i]
            #i, i+i, ... len(s)까지 간다
            for j in range(i, len(s)+i, i):
                #잘라낸 값이 temp와 같다면 카운트 증가
                if temp==s[j:i+j]:
                    cnt+=1
                #잘라낸 값과 다르다면 shorten에 입력하고 다음 글자로 넘어감
                #맨 마지막 string까지 본 경우는 여기로 오게 된다.
                #s[len(s):] -> 결과는 공백
                else:
                    if cnt == 1:
                        shorten += temp
                    else:
                        shorten += str(cnt) + temp
                    cnt = 1
                    temp=s[j:j+i]

            # print(shorten)
            answer = min(answer, len(shorten))
        return answer