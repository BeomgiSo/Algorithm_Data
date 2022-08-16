import heapq
import sys
input = sys.stdin.readline
hq = []
N = int(input())

for _ in range(N):
    x = int(input())
    if x == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(-heapq.heappop(hq))
    heapq.heappush(hq, -x)