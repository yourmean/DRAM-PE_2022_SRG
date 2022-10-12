import itertools

def ban_check(sui, banned_id):
    for i in range(len(sui)):
        if len(sui[i]) != len(banned_id[i]):
            return False
        for j in range(len(cb[i])):
            if banned_id[i][j] != '*' and sui[i][j] != banned_id[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    cnt = 0
    result = []
    answer = []
    set_user_id = list(itertools.permutations(user_id, len(banned_id)))
    for sui in set_user_id:
        if ban_check(sui, banned_id):
            cb = list(cb)
            cb = sorted(cb)
            result.append(cb)
    for i in result:
        if not i in answer:
            answer.append(i)
    return len(answer)
