N = int(input())
arr = []
arr = list(map(int,input().split(" ")))

sortArr = sorted(list(set(arr)))
dictionary = dict()
for index in range(len(sortArr)):
    dictionary[sortArr[index]] = index
for x in arr:
    print(dictionary[x],end=" ")
