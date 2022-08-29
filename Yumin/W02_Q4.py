# 이서희, 이세휘, 이승훈 (선배님)

import numpy as np

def groupAnagrams(strs):

    # 초기화
    results = []
    hangeul = [""] * len(strs)

    # 단어에 포함된 초성 리스트 만들기
    for index, word in enumerate(strs):
        A = list(word)
        A.sort()
        hangeul[index] = str(A)

    # 그룹 만들기
    hangeul_unique = list(set(hangeul))

    # 같은 애너그램을 가진 단어끼리 묶기
    for n in range(len(hangeul_unique)):
        # 같은 애너그램을 가진 단어의 인덱스 모두 찾기
        hangeul = np.array(hangeul)
        indexes = np.where(hangeul == hangeul_unique[n])[0]
        # 같은 그룹으로 묶기
        new = []
        for i in indexes:
            new.append(strs[i])
        results.append(new)

    return len(results)


# 입력으로 단어의 수, 단어들을 받음
num_strs = int(input())
strs = []
for _ in range(num_strs):
    strs.append(input())

print(groupAnagrams(strs))