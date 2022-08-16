N=int(input())
data1 = list(map(int,input().split()))
data = list(set(data1))

data.sort()
dict_={}

for i,v in enumerate(data):
    dict_[v] = i

result = []
for i in data1:
    result.append(dict_[i])

print(*result)