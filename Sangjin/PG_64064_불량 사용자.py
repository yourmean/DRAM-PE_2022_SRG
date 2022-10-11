from itertools import permutations


def ban_check(group, banned_id):
    #group의 표현형: ('frodo', 'fradi')
    for i in range(len(group)):
        #가져온 group과 banned_id의 길이 비교
        if len(group[i]) != len(banned_id[i]):
            return False
        for j in range(len(group[i])):
            #group과 banned_id의 글자를 하나씩 비교
            #다른지 확인하고 "*"는 그대로 진행
            if group[i][j] != banned_id[i][j]:
                if banned_id[i][j] != "*":
                    return False
    return True

def solution(user_id, banned_id):
    
    answer = 0
    answer_set = []
    
    #permutation 사용: user_id의 서로 다른 n 개 중 r 개를 골라 순서를 정해 나열
    #확인용: list(permutations(user_id, len(banned_id)))
    #결과: [('frodo', 'fradi'), ('frodo', 'crodo') ... ()]
    for group in permutations(user_id, len(banned_id)):
        if ban_check(group, banned_id):
            #겹치는지 판별, set 형태로 저장
            if set(group) not in answer_set:
                answer_set.append(set(group))
                
    answer = len(answer_set)
    
    return answer