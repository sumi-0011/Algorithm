# 2022-01-31
global targetNumber,gNumbers;

def func(index, minus, oldValue):
    global targetNumber, gNumbers;
    # print(index,minus,oldValue)

    if minus:
        #음수경우
        newValue = oldValue-gNumbers[index]
    else:
        newValue = oldValue + gNumbers[index]
    if len(gNumbers) == index+1:
        if targetNumber == newValue:
            # print("!!!!!!!!!!!!!!!!!!!!!!")
            return 1;
        else:
            return 0
    else :
        count = 0
        count +=func(index + 1, True, newValue)
        count +=func( index + 1, False, newValue)
        return count
def solution(numbers, target):
    global targetNumber,gNumbers;
    gNumbers = numbers;
    targetNumber = target
    answer = 0
    answer+=func(0,True,0)
    answer+=func(0,False,0)

    return answer

if __name__ == '__main__':
    numbers = [4, 1, 2, 1]
    target = 4
    print(solution(numbers,target))