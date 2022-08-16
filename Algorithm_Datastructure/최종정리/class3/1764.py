import sys
input = sys.stdin.readline
N , M = list(map(int,input().split()))
data_1 = set()
data_2 = set()

for _ in range(N):
    x = input().rstrip()
    data_1.add(x)

for _ in range(M):
    t = input().rstrip()
    data_2.add(t)
inter = list(data_1.intersection(data_2))
print(len(inter))
inter.sort()
print(*inter)
# 시간 초과