import sys
M,N = map(int,input().split(" "))
numDict = {}
strDict = {}
for i in range(M):
    str = sys.stdin.readline().strip()
    numDict[i+1] = str
    strDict[str] = i+1


# print(numDict)
# print(strDict)
for _ in range(N):
    inputStr = sys.stdin.readline().strip()
    if inputStr.isdigit():
        #숫자이면
        print(numDict[int(inputStr)])
    else:
        print(strDict[inputStr])

        #그지같은 시간복잡도 ;;