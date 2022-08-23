# 엘리스 스택 큐 주분 받기
from collections import deque

prior = deque()
general = deque()
N = int(input())

for i in range(N):
    data = list(map(int,input().split()))
    if data[-1] == 0:
        general.append([i+1] + data[:-1])
    else:
        prior.append([i+1]+data[:-1])
time = 0
result = []
#print(prior,general,len(prior),len(general))
while len(general)!=0:
    time+=1
    while len(prior) != 0:
        prior_temp = prior[0]
        if time >= prior_temp[1]:
            prior_temp = prior.popleft()
            time +=prior_temp[2]
            result.append(prior_temp[0])
        else:
            break
            
    general_temp = general[0]
    if time >= general_temp[1]:
        general_temp = general.popleft()
        time += general_temp[2]
        result.append(general_temp[0])
    else:
        continue

print(result)
