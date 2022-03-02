from collections import deque

def dfs(graph,start):
    stack = [start]
    visited = []

    while stack:
        x = stack.pop()
        if x not in visited:
            # print(x,stack,sorted(graph[x]))

            visited.append(x)
            stack = stack +list(reversed(graph[x]))
            stack = stack + graph[x]
    return visited
def bfs(graph, start):
    queue = deque([start])
    visited = []
    while queue:
        x = queue.popleft()
        if x not in visited:
            visited.append(x)
            queue.extend(graph[x])
    return visited
if __name__ == '__main__':
    N, M, V = map(int, input().split(" "))
    graph = dict()
    for _ in range(M):
        a, b = map(int, input().split(" "))
        # graph에 추가
        if a in graph:
            graph[a] = graph[a] +[b]
        else:
            graph[a] = [b]
        if b in graph:
            graph[b] = graph[b]+[a]
        else:
            graph[b] = [a]
    # print(graph)
    result1 = dfs(graph,V)
    result2 = bfs(graph,V)
    for x in result1:
        print(x,end=" ")
    print()
    for x in result2:
        print(x,end=" ")
