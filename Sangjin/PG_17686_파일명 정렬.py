def solution(files):
    answer = []

    #파일명을 Head, Number로 나누어 저장하는 곳
    New_files = [] #[원본, Head, Number]순서


    for i in range(len(files)):
        New_files.append([files[i]])
        #Head 부분을 저장
        H = ""
        for s in files[i]:
            if s.isdigit():
                break
            else:
                H += s
        New_files[-1].append(H.lower()) #소문자로 통일하여 저장

        N = ""
        digit_start = False
        for s in files[i]:
            if s.isdigit():
                digit_start = True
                N += s
            elif digit_start: #숫자 부분이 끝난 경우
                break
        New_files[-1].append(int(N)) #숫자 형식으로 저장


    #Head 기준으로 먼저 정렬, Number 기준으로 다음 정렬
    New_files = sorted(New_files, key = lambda x : (x[1], x[2]))

    #정렬된 순서대로 answer list에 입력
    answer = [New_files[i][0] for i in range(len(New_files))]

    return answer