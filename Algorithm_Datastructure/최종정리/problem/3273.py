N = int(input())
data = list(map(int,input().split()))
x = int(input())
data.sort()

left = 0
right = N - 1
cnt = 0

while left < right:
    temp = data[left] + data[right]
    #print(left,right,temp)
    if  temp == x:
        cnt+=1
        
    
    if temp < x:
        left+=1
    else:
        right-=1
print(cnt)
# x = int(input())
# cnt = 0
# for i in range(len(data)-1):
#     for j in range(i+1,len(data)):
#         if data[i]+data[j] == x:
#             cnt+=1

# print(cnt)
