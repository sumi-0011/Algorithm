# 숨박꼭질

N, K = map(int,input().split(" "))
cnt =0
# N이 작은수
if N > K : (N,K) = (K,N)

while N * 2 <= K:
    cnt +=1
    N *=2

print(cnt + (K-N))