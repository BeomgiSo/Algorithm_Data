N = int(input())
data = list(map(int,input().split()))

import heapq
heap = []
for i in data:
    heapq.heappush(heap,i)

sum_ = 0
wait_time = []
for _ in range(len(data)):
    temp = heapq.heappop(heap)
    sum_+=temp
    wait_time.append(sum_)

print(sum(wait_time))
