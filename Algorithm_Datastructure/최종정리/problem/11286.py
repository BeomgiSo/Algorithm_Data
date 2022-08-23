import heapq as hq
import sys
input = sys.stdin.readline
N = int(input())
data = []
for _ in range(N):
    x=int(input())
    if x == 0:
        if len(data) !=0:
            temp = hq.heappop(data)
            print(temp[1])
        else:
            print(0)
    else:
        hq.heappush(data,(abs(x),x))
