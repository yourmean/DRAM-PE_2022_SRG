def solution(record):
    userDict = {}
    answer = []

    for line in record:
        line = line.split(" ")

        if line[0] == "Enter":
            userDict[line[1]] = line[2]
        elif line[0] == "Change":
            userDict[line[1]] = line[2]

    for line in record:
        line = line.split(" ")
        targetString = userDict[line[1]]
        if line[0] == "Enter":
            targetString += "님이 들어왔습니다."
        elif line[0] == "Leave":
            targetString += "님이 나갔습니다."
        else:
            continue
        answer.append(targetString)

    return answer