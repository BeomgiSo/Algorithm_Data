N = int(input())
dict_= {}

for  i in range(1,int(N**(1/2))+1):
    dict_[i] = i**2

from itertools import combinations
list_ = list(dict_.keys())
j=0
answer = 0
while True:
    j+=1
    for i in combinations(list_,j):
        sum = 0
        for k in i:
            sum+=dict_[k]
        if sum == N:
            answer = j
            break
        
    if answer !=0:
        print(answer)
        break


        