#듣보잡
N,M = map(int,input().split(" "))
arr1 = []
for _ in range(N+M):
    arr1.append(input())
arr1.sort()
old=''
result = []
for x in arr1:
    if old == x:
        result.append(x)
    old =x

#출력
print(len(result))
for x in result:
    print(x)