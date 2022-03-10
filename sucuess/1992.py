# 컴퓨터를 연결하는 비용을 최소로 하여야 한다.
# 모든 컴퓨터를 연결하는데 필요한 최소 비용을 출력하면됨
# 비용을 최소로 해서 모든 컴퓨터를 연결하ㅏ면 된다고 하니 신장트리를 크루스칼 알고리즘으로 찾으면 될것 같다.

def find(parent,u):
    if u!=parent[u]:
        parent[u] = find(parent,parent[u])
    return parent[u]

def union(parent,u,v):
    root1 = find(parent,u)
    root2 = find(parent,v)
    parent[root2] = root1

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    graph = []
    parent = [0] * (N + 1)
    result = 0
    for _ in range(M):
        a,b,c = map(int,input().split(" "))
        graph.append((a,b,c))
    graph  = sorted(graph,key=lambda x:x[2])
    for i in range(1, N + 1):
        parent[i] = i
    for x in graph:
        a,b,cost = x
        #사이틀이 발생하지 않으면 집한에 포함
        if find(parent,a) != find(parent,b):
            union(parent,a,b)
            result +=cost

    print(result)