# 출처 : https://velog.io/@minnseong/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%B0%A8-%EC%9A%94%EA%B8%88-%EA%B3%84%EC%82%B0

import math


def dateToMinutes(date):
    h, m = map(int, date.split(':'))
    return h * 60 + m


def solution(fees, records):
    answer = []

    # 기본 시간, 기본 요금, 단위 시간, 단위 요금 순
    dt, df, ut, uf = fees

    dic = dict()

    for r in records:
        time, number, history = r.split()
        number = int(number)

        if number in dic:
            dic[number].append([dateToMinutes(time), history])
        else:
            dic[number] = [[dateToMinutes(time), history]]

    rList = list(dic.items())
    rList.sort(key=lambda x: x[0])

    for r in rList:
        t = 0

        for rr in r[1]:
            if rr[1] == "IN":
                t -= rr[0]
            else:
                t += rr[0]

        if r[1][-1][1] == "IN":
            t += dateToMinutes('23:59')

        if t <= dt:
            answer.append(df)
        else:
            answer.append(df + math.ceil((t - dt) / ut) * uf)

    return answer