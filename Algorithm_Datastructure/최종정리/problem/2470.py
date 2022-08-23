
#data = list(map(int,input().split()))
import math
data = [-2,-99,-1,4,98]
data.sort()
left = 0
right = len(data) - 1
target = 0
print(data)
while left < right:
    temp = data[left]+data[right]
    a = abs(temp)
    b = data[left+1]+data[right]
    c = data[left]+data[right-1]
    if a == target:
        print(data[left],data[right])
    elif a > b:


