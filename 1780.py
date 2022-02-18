import sys
def func(arr,x,y,length):
    # [row[j:j+m] for row in field[i:i+n]]
    now_arr = [row[y:y+length] for row in arr[x:x+length]]
    cnt0 = 0
    cnt1 = 0
    for row in now_arr:
        cnt0+=row.count(0)
        cnt1+=row.count(1)

    if cnt0 == length * length:
        return [0]
    if cnt1 == length * length:
        return [1]
    if cnt0 == 0 and cnt1 ==0:
        return [-1]
    result = []
    new_length = length //3
    for i in range(0,3):
        for j in range(0,3):
            result += func(now_arr, i*new_length, j*new_length, new_length)
    return result


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int,sys.stdin.readline().split(" "))))
    # print(arr)
    # arr = [[0, 0, 0, 1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 1, -1, -1, -1], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, -1, 0, 1, -1, 0, 1, -1], [0, -1, 1, 0, 1, -1, 0, 1, -1], [0, 1, -1, 1, 0, -1, 0, 1, -1]]
    result = func(arr, 0, 0, len(arr))
    print(result.count(-1))
    print(result.count(0))
    print(result.count(1))
