def solution(files):
    answer = []
    for ss in files:
        head, number, tail = '', '', ''

        number_check = False
        for i in range(len(ss)):
            if ss[i].isdigit():
                number += ss[i]
                number_check = True
            elif not number_check:
                head += ss[i]
            else:
                tail = ss[i:]
                break
        answer.append((head, number, tail))

    answer.sort(key = lambda x: (x[0].upper(), int(x[1])))

    return [''.join(t) for t in answer]
