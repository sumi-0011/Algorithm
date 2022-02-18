N = int(input())
M = int(input())
S = input()
patternCount = 0
count = 0
index= 1
while index < M-1:
    #1~m-2까지
    if S[index-1] == 'I' and S[index] == 'O' and S[index+1] == 'I':
        patternCount +=1
        if patternCount >=N:
            count+=1
        index+=1
    else :
        patternCount = 0
    index+=1
print(count)