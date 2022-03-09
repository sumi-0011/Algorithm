def solution(lines):
    #초당 최대 처리량은 요청의 응답 완료 여부에 관계없이 임의 시간부터 1초(=1,000밀리초)간 처리하는 요청의 최대 개수를 의미
    # line => 응답완료시간 S와 처리시간 T가 공백으로 구분
    list = []
    totalList = []
    for line in lines:
        #2016-09-15 03:10:33.020 0.011s
        splitLineList= line.split(" ")
        hh, mm, ss = splitLineList[1].split(":") #hh:mm:ss.sss
        T = splitLineList[2].replace("s","")    #초단위 s 제거
        #시작 초
        # start = int(hh) * 3600 + int(mm) * 60 + float(ss) - float(T) + 0.001 #한시간은 60분 , 1분은 60초
        # during = float(T) - 0.001
        start =  (int(hh) * 3600 + int(mm) * 60 + float(ss) - float(T)) * 1000 +1
        end  = (int(hh) * 3600 + int(mm) * 60 + float(ss)) * 1000

        list.append((int(start), int(end)))
        totalList.append(int(start))
        totalList.append(int(end))
        # print(start,T)

    # 탐색해야 할 시작 초와 끝 초를 찾는다.
    startSecond = list[0][0]
    endSecond = list[len(list)-1][1]
    answer = []
    # for time in range(startSecond , endSecond ):    #소수점 제거
    for time in totalList:
        #list를 돌면서 해당되는 time 수 세기
        cnt =0
        for index in range(0, len(list)):
            start = list[index][0]
            end = list[index][1]
            if end < time:
                continue
            if start >= time + 1000:
                continue
            # break , 시간복잡도 통과
            if start > time + 1000:
                break
            cnt +=1
        answer.append((cnt,time))

    return max(answer)[0]

if __name__ == '__main__':
    lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]

    print(solution(lines))
