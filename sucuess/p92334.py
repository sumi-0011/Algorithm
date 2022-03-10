def solution(id_list, report, k):
    answer = []

    report_count = dict()   # 신고 횟수 저장
    emailCnt = dict()
    # report_count 초기화 : 신고 0, 신고 user list 빈배열
    for x in id_list:
        report_count[x] = (0,[])
        emailCnt[x] = 0
        
    # 신고 내용 취합
    for x in report:
        user, userToReport = x.split(" ")
        # 신고당한 횟수, 신고한 user 리스트
        if user in report_count[userToReport][1]:
            continue
        report_count[userToReport] = (report_count[userToReport][0]+1, report_count[userToReport][1]+[user])

    for cnt, userList in report_count.values():
        if k <= cnt:
            for x in userList:
                emailCnt[x] +=1
    # print(report_count)
    # print(emailCnt)
    for x in id_list:
        answer.append(emailCnt[x])
    return answer

if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2
    print( solution(id_list, report, k))