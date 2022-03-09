def solutuion(N, r,c):
    #탈출
    if N == 0:
        return 0
    N -=1
    result = 0
    # 1
    if r <  2**N and c < 2 ** N:
        result = solutuion(N,r,c)
    # 2
    elif r < 2** N :
        c -= 2**N
        result = solutuion(N,r,c) + (2**N) ** 2 * 1
    #3
    elif c < 2 **N:
        r -= 2 ** N
        result = solutuion(N,r,c) + (2**N) ** 2 * 2
    else:
        r -= 2 ** N
        c -= 2 ** N
        result = solutuion(N,r,c) + (2**N) ** 2 * 3
    return result

if __name__ == '__main__':
    N, r,c = map(int, input().split(" "))
    print(solutuion(N,r,c))
