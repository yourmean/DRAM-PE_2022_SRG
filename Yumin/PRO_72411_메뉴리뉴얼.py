# https://velog.io/@djagmlrhks3/Algorithm-Programmers-%EB%A9%94%EB%89%B4-%EB%A6%AC%EB%89%B4%EC%96%BC-by-Python

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for c in course:
        tmp = []
        for order in orders:
            for o in combinations(order, c):
                tmp.append(''.join(sorted(o)))
        sorted_order = Counter(tmp).most_common()
        print(sorted_order)
        answer += [menu for menu, cnt in sorted_order if cnt > 1 and cnt == sorted_order[0][1]]

    return sorted(answer)