# import sys
# input = sys.stdin.readline
# dict_ = {}
# N,M = list(map(int,input().split()))

# for i in range(N):
#     x = input()
#     dict_[x] = i+1

# for _ in range(M):
#     x=input()
#     if x.isalpha() == True:
#         print(dict_[x])
#     else:
#         for i in dict_.keys():
#             if i == int(x.rstrip()):
#                 print(dic_.values()[i])
#                 break
N,M = list(map(int,input().split()))
data = []
for i in range(N):
    x = input()
    data.append(((i+1),x))

for i in range(M):
    y = input()
    if y.isal == y:

