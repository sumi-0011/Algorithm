def dfs10026( i,j,target,flag,array,visited):
    # flag 1 : target , flag 2: 'R,G'
    stack = list()
    stack.append((i,j))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while stack:
        idx,jdx = stack.pop()
        if idx <0 or jdx < 0 or idx >= len(arr) or jdx >=len(arr):
            continue
        if( (flag == 1 and array[idx][jdx] == target) or \
                (flag == 2 and (array[idx][jdx] == "R" or array[idx][jdx] == "G"))) \
                and not visited[idx][jdx]:
            visited[idx][jdx]= True
            for x in range(4):
                stack.append((idx + dx[x], jdx + dy[x]))
    return visited
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input()))

visited = [[False for _ in range(n)] for _ in range(n)]
visited2 = [[False for _ in range(n)] for _ in range(n)]

cnt = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt +=1
            visited = dfs10026(i,j,arr[i][j],1,arr,visited)
        if not visited2[i][j]:
            cnt2 +=1
            if arr[i][j] == 'B':
                visited2 = dfs10026(i, j, arr[i][j], 1, arr, visited2)
            else :
                visited2 = dfs10026(i, j, arr[i][j], 2, arr, visited2)

print(cnt,cnt2)
