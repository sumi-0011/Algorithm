
#https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3
# 2022-01-31
def dfs(graph, start_node,visited):
    ## 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    need_visited= list()
    need_visited.append(start_node)
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            for i in range(0, len(graph[node])):
                if graph[node][i] == 1:
                    # need_visited.extend(graph[node])
                    need_visited.append(i)
            # print(node,need_visited,graph[node])
    return visited
def solution(n, computers):
    answer = 0
    visited = []
    for x in range(n):
        if not x in visited:
            answer+=1;
            visited = dfs(computers,x,visited)

    return answer

if __name__ == '__main__':
    n=3
    computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print( solution(n,computers))