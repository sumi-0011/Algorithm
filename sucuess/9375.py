T = int(input())
for _ in range(T):
    N = int(input())
    dict = {}
    for _ in range(N):
        name, type = map(str, input().split(" "))
        if type in dict:
            dict[type] = dict[type] + [name]
        else :
            dict[type] =  [name]
    result = 1
    for k,v in dict.items():
        result *= len(v) +1
    print(result-1)