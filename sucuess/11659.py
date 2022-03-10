#sys.stdin.readline().split()
import sys
N,M = map(int,input().split(" "))
arr = list(map(int,input().split(" ")))
sum_arr = [arr[0]]
for i in range(1,len(arr)):
    sum_arr.append(sum_arr[i-1]+arr[i])
# print(sum_arr)
for _ in range(M):
    i,j = map(int,sys.stdin.readline().split(" "))
    if i-2 <0 :
        print(sum_arr[j-1])
    else :
        print(sum_arr[j-1] -sum_arr[i-2])