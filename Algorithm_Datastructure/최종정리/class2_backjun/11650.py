import sys
input = sys.stdin.readline
N = int(input())
data =  []
for _ in range(N):
    x,y = list(map(int,input().split()))
    data.append([x,y])



result = sorted(data,key = lambda x : x[1] if x[1]])

for i in result:
    print(*i)