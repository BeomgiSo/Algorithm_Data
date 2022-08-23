from collections import deque
import sys
#input = sys.stdin.readline
N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))

for i in range(len(data)):
    left = data[:i]
    right = data [i+1:]
    pivot = data[i]
    cnt = 0
    print(left,right)
    if len(left) != 0:
        for j in range(len(left),-1,-1):
            if pivot <= left[j]:
                cnt+=1
            else:
                break
            
    if len(right) !=0:
        for j in range(i,len(right)):
            if pivot <= right[j]:
                cnt+=1
            else:
                break
        
    print(cnt,pivot)










# max_v = -float("inf")
# x=deque()
# while data:
#     temp = data.popleft()
#     cnt = 1
#     for i in data:
#         if i >= temp:
#             cnt +=1
#         else:
#             break
        
#     for i in x:
#         if i >= temp:
#             cnt+=1
#         else:
#             break    
#     x.appendleft(temp)

#     if cnt != 1:
#         area = cnt*temp
#     else:
#         area = cnt * temp
#     #print("temp",temp,"area",area)
#     max_v = max(area,max_v)

print(max_v)