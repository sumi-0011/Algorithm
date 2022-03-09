def solution(record):

    nickname = dict()
    behaviorList = dict()
    index = 0
    for x in record:
        splitList = x.split(" ")
        command  = splitList[0]
        userId= splitList[1]
        if command == 'Enter':
            nickname[userId] =  splitList[2]   # 들어올때 입력한 닉네임으로 설정
            if userId in behaviorList:
                #이미 추가 된 적이 있는 유저의 경우
                behaviorList[userId].append((index,command))  #행동에 추가
            else:
                behaviorList[userId] = [(index,command)]
            index += 1
        if command== 'Leave':
            # 유저의 행동 리스트에 나가기를 추가
            behaviorList[userId].append((index, command))
            index += 1
        if command == 'Change':
            #유저의 닉네임을 입력한 것으로 바꾸고
            # 행동에 추가
            nickname[userId] = splitList[2]
            # behaviorList[userId].append((index, command))

    # print(nickname)
    # print(behaviorList)
    answer = [""] * index #행동의 개수만큼 초기화
    #원하는 형식으로 출력하여 answer에 추가
    for userId in nickname:
        for index, behavior in behaviorList[userId]:
            if behavior == 'Enter':
                answer[index] = nickname[userId] +"님이 들어왔습니다."
            if behavior == 'Leave':
                answer[index] = nickname[userId] +"님이 나갔습니다."
    return answer

if __name__ == '__main__':
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))
