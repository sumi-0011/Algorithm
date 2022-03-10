


if __name__ == '__main__':
    # 초기값 : 1,1,1,2,2
    p = [1, 1, 1, 2, 2]

    T = int(input())
    for _ in range(T):
        N = int(input())
        if len(p) > N-1:
            print(p[N-1])
        else:
            for x in range(len(p)+1,N+1):
                p.append(p[x-2]+p[x-6])
            print(p[N-1])