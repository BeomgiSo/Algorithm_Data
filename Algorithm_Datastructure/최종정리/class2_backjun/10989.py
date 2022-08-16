import heapq
# 메모리 초과...
# hq = []
# N = int(input())

# for _ in range(N):
#     x = int(input())
#     heapq.heappush(hq, x)

# for i in range(N):
#     result = heapq.heappop(hq)
#     print(result)

list_= [0] * 10001
N = int(input())
for _ in range(N):
    x= int(input())
    list_[x] +=1

for i in range(len(list_)):
    if list_[i] == 0:
        continue
    else:
        for _ in range(list_[i]):
            print(i)