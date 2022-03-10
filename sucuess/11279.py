import heapq,sys
N = int(input())
heap = []
for _ in range(N):
    input = int(sys.stdin.readline().strip())
    if input == 0:
        try:
            n = heapq.heappop(heap)[1]
            print(n)
        except IndexError:
            print(0)

    else:
        heapq.heappush(heap,(-input,input))
