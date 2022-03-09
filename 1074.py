def func(n, point,x,y) :
    num = n//2
    # | 0 | 1 |
    # | 2 | 3 |
    # 0번 영역
    if num + x > point[0] and num + y > point[1]:
        index = 0
    # 1번 영역
    elif num + x > point[0]:
        index = 1
    # 2번 영역
    elif num + y > point[1]:
        index = 2
    # 3번 영역
    else:
        index = 3
    print(n,index,point,x,y)
    if n == 2 :
        # 탈출 조건
        index = point[0] %2 * 2 + point[1] %2
        return index
    else :
        if index%2==1:
            x += num
        if index>=2 :
            y +=num
        return func(num, point,x ,y) + (num ** 2) * index

if __name__ == '__main__':
    N, r,c = map(int, input().split(" "))
    print(func(2**N, (r,c),0,0))
