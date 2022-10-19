def solution(s):
    answer = [len(s)]

    for l in range(1, len(s) // 2 + 1):
        tmp = ''
        cnt = 1
        a = s[:l]

        for i in range(l, l + len(s), l):
            if a == s[i:i + l]:
                cnt += 1
            else:
                tmp += a if cnt == 1 else str(cnt) + a
                a = s[i:i + l]
                cnt = 1

        answer.append(len(tmp))
    return min(answer)