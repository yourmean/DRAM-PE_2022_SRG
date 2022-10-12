import re

def solution(files):
    # NUMBER 기준 1차 정렬
    s1 = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))

    # HEAD 기준 2차 정렬
    s2 = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])

    return s2